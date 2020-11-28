import threading
from typing import List

from sanic.request import Request
from sanic.response import HTTPResponse, json
from sanic.exceptions import abort

from ..classes.view import View
from ..utils.filter import filter_sentences, filter_duplicates
from ..utils._id import IDmemory  # id 기반 dict memory

from ..textAnalyzer.text_comparison.checking import init, Check


def init_text_comparison():
    """
    Calls textAnalyzer.text_comparison.checking.init().
    """
    global idm
    idm = IDmemory()  # id 기반 dict memory
    init()


class CheckView(View):
    base_path = '/check'
    
    async def post(self, request: Request) -> HTTPResponse:
        """
        POST /check
        Returns the checked data.
        """
        sentences: List[str] = request.json["sentences"]
        sentences = filter_duplicates(  # (순서 유지) 중복 제거
            filter_sentences(  # 띄어쓰기 적은 것들 거르기
                sentences
            )
        )

        # 분석
        ch = Check()
        _id = idm.add(ch)
        _thread = threading.Thread(target=ch.check, args=(sentences,))
        _thread.start()  # 오류 검출 (스레드)

        response = {
            "id": _id
        }

        response = json(response)
        return response


class CheckIDView(View):
    base_path = '/check/progress'  # /check/progress?id=1234asdf

    async def get(self, request: Request) -> HTTPResponse:
        # _id = tag  # :id가 뭔지는 난 잘 모르겠다
        query_args = request.query_args()
        if not query_args:
            abort(400)
        if len(query_args[0]) != 2:  # [["id", "1234asdf"]]
            abort(400)

        if query_args[0][0] != 'id':
            # wrong request parameter
            abort(400)
        _id = query_args[0][1]

        try:
            ch: Check = idm[_id]
        except KeyError:
            # _id가 메모리에 없을 때
            abort(400)
        
        sentences = [d['origin'] for d in ch.response]

        response = {
            "sentences": sentences,  # 오류 문장
            "progres": ch.progress,  # 처리된 문장 개수
            "isDone": ch.finished
        }

        if ch.finished:
            # 분석 끝났으면? -> 메모리에서 제거
            idm.delete(_id)

        response = json(response)
        return response

"""
id 기반 메모리를 관리한다.
"""
import random
import string

class IDmemory:
    def __init__(self) -> None:
        self.memory: dict = {}  # 메모리 형식 {id: value}
        self.opt: dict = {
            'id_len': 30  # id 길이
        }

    def random_string(self, len: int) -> str:
        # 무작위 알파벳을 배열한 string을 반환한다.
        # ex) f(3) -> 'bwf'
        return ''.join([random.choice(string.ascii_lowercase + string.digits) \
                        for _ in range(self.opt['id_len'])])
    
    def gen_id(self) -> str:
        # id 생성
        _id: str = self.random_string(self.opt['id_len'])  # id 생성
        while _id in self.memory:
            # 이미 존재하는 id일 경우? -> 다른 거 생성
            _id = self.random_string(self.opt['id_len'])
        return _id

    def add(self, value) -> str:
        # memory에 value 추가
        _id = self.gen_id()  # id 생성
        self.memory[_id] = value
        return _id

    def delete(self, _id: str) -> None:
        try:
            del self.memory[_id]
        except KeyError:
            # 해당 id가 memory에 없으면?
            pass

    def __str__(self) -> str:
        # memory 반환
        return str(idm.memory)

    def __getitem__(self, slice):
        return self.memory[slice]


if __name__ == "__main__":
    idm = IDmemory()
    idm.add('test')
    _id = idm.add('hi')
    idm.add(1222)
    print(idm)
    print(idm[_id])

from typing import List
from sanic.request import Request
from sanic.response import HTTPResponse, json
from ..utils.filter import filter_sentences

async def check(request: Request) -> HTTPResponse:
    """
    Returns the checked data.
    """
    sentences: List[str] = request.json["sentences"]
    sentences = filter_sentences(sentences)

    response = [
        {
            "origin": s,
            "is_wrong": True,
            "category": "dokdo",
            "corrected": "Corrected sentence",
            "confidence": 0.8,
        }
        for s in sentences
    ]
    
    response = json(response)
    return response

from typing import List
from sanic.request import Request
from sanic.response import HTTPResponse, json

async def check(request: Request) -> HTTPResponse:
    sentences: List[str] = request.json["sentences"]

    response = []
    for s in sentences:
        response.append(
            {
                "origin": s,
                "is_wrong": True,
                "category": "dokdo",
                "corrected": "Corrected sentence",
                "confidence": 0.8,
            }
        )
    
    response = json(response)
    return response

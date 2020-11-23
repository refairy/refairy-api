from sanic.request import Request
from sanic.response import HTTPResponse, json

async def check(request: Request) -> HTTPResponse:
    response = json(
        {
            "origin": request.json["sentence"],
            "is_wrong": True,
            "category": "dokdo",
            "corrected": "Corrected sentence",
            "confidence": 0.8,
        }
    )
    return response

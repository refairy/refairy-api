from sanic.request import Request
from sanic.response import HTTPResponse, text

async def index(request: Request) -> HTTPResponse:
    return text("Hello, ReFairy!")

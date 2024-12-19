from fastapi.responses import JSONResponse
from fastapi import Request
from typing import Any, Optional


class ApiResponse:
    message: str
    code: int
    data: Optional[Any]

    def __init__(
        self, message: str = None, data: Optional[Any] = None, code: int = None
    ):
        self.message = message
        self.code = code
        self.data = data

    def __to_dict(self) -> dict:
        return {"message": self.message, "code": self.code, "data": self.data}

    def to_json(self) -> dict:
        return JSONResponse(content=self.__to_dict(), status_code=self.code)


class ResponseSuccess(ApiResponse):
    def __init__(
        self, message: str = None, data: Optional[Any] = None, code: int = 200
    ):
        super().__init__(message=message, data=data, code=code)


class ResponseFailure(ApiResponse, Exception):
    def __init__(
        self, message: str = None, data: Optional[Any] = None, code: int = 400
    ):
        super().__init__(message=message, data=data, code=code)


async def api_failure_handler(_: Request, error: ResponseFailure):
    return error.to_json()

from typing import Any, Optional
from pydantic import BaseModel
from fastapi.responses import JSONResponse


class Responser:
    def __init__(self, data: Optional[Any] = None):
        self.__data = data

    def __msg(self, msg: str, code: int):
        return {
            "message": msg,
            "data": self.__data,
            "code": code
        }

    def _response(self, message: str, code: int) -> JSONResponse:
        return JSONResponse(content=self.__msg(message, code), status_code=code)

    def response_200(self) -> JSONResponse:
        return self._response("OK", 200)

    def response_201(self) -> JSONResponse:
        return self._response("Created", 201)

    def response_400(self,msg: str = "Bad Request") -> JSONResponse:
        return self._response(msg, 400)

    def response_401(self) -> JSONResponse:
        return self._response("Unauthorized", 401)

    def response_403(self) -> JSONResponse:
        return self._response("Forbidden", 403)

    def response_404(self) -> JSONResponse:
        return self._response("Not Found", 404)

    def response_405(self) -> JSONResponse:
        return self._response("Method Not Allowed", 405)

    def response_409(self) -> JSONResponse:
        return self._response("Conflict", 409)

    def response_411(self) -> JSONResponse:
        return self._response("Length Required", 411)

    def response_412(self) -> JSONResponse:
        return self._response("Precondition Failed", 412)

    def response_429(self) -> JSONResponse:
        return self._response("Too Many Requests", 429)

    def response_500(self) -> JSONResponse:
        return self._response("Internal Server Error", 500)

    def response_503(self) -> JSONResponse:
        return self._response("Service Unavailable", 503)

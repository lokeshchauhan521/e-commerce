from fastapi import Request, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError


class CustomException(Exception):
    def __init__(self, message: str, code: int = status.HTTP_400_BAD_REQUEST):
        self.message = message
        self.code = code


async def custom_exception_handler(request: Request, exc: CustomException):
    return JSONResponse(
        content={"message": "Something went wrong", "data": None, "code": 200},
        status_code=exc.code,
    )

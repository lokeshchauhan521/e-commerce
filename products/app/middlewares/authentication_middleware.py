from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from app.core.utils.api_response import ResponseFailure
from app.core.utils.auth import decode_access_token
from app.routes.get_route_map import secured_routes


class AuthenticationMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        print(request.url.path, secured_routes)
        if secured_routes.count(request.url.path.rstrip("\\")):
            try:
                authorization: str = request.headers.get("Authorization")
                if not authorization or not authorization.startswith("Bearer "):
                    raise Exception()

                token = authorization.split(" ")[1]  # Extract token from "Bearer <token>"
                user = decode_access_token(token)

                if not user:
                    raise Exception()

                request.state.user = user

            except Exception as e:
                return ResponseFailure(
                    "Authentication failed.",
                    code=401,
                ).to_json()

        response = await call_next(request)
        return response

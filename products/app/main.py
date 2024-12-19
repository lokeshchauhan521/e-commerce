from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware
# from .routes.get_route_map import routing
from .core.config.db import Base, engine
from .core.utils.api_response import ResponseFailure, api_failure_handler
# from .middlewares.authentication_middleware import AuthenticationMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI()

# routing(app)

# app.add_middleware(AuthenticationMiddleware)

app.add_exception_handler(ResponseFailure, api_failure_handler)

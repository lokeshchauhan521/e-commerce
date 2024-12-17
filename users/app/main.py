from fastapi import FastAPI
from .routes.get_route_map import routing
from .core.config.db import Base, engine
from .core.utils.api_response import ResponseFailure, api_failure_handler

Base.metadata.create_all(bind=engine)

app = FastAPI()

routing(app)

app.add_exception_handler(ResponseFailure, api_failure_handler)

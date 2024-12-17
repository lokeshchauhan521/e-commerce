from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from .routes.get_route_map import routing
from .core.config.db import Base, engine
from .core.utils.exception_handler import CustomException, custom_exception_handler

Base.metadata.create_all(bind=engine)

app = FastAPI()

routing(app)

app.add_exception_handler(CustomException, custom_exception_handler)

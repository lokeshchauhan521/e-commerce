import os
from fastapi import FastAPI
from ..routes.get_route_map import routing

def create_app():
    app = FastAPI()
    routing(app)
    return app
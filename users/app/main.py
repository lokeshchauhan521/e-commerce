from fastapi import FastAPI
from .routes.get_route_map import routing

app = FastAPI()

routing(app)

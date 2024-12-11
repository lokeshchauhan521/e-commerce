from dotenv import load_dotenv
from fastapi import FastAPI

from .routes.get_route_map import routing

load_dotenv()

app = FastAPI()

routing(app)

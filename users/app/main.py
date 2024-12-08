from fastapi import Depends, FastAPI
from .routes.get_route_map import routing
from .app_config.app_config import create_app

app = create_app()


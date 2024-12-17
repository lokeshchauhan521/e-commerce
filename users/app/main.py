from fastapi import FastAPI
from .routes.get_route_map import routing
from .core.config.db import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

routing(app)

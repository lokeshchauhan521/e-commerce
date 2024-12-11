from app.core.auth.dependencies import get_current_user
from app.services.login import Login
from fastapi import Depends
from fastapi_utils import Api

from ..services.create_user import CreateUser
from ..services.get_user import GetUser
from ..services.home import Home
from ..services.test import Test


def get_route_map():
    return [
        {
            "router": Home(),
            "path": "/",
            "dependencies": [],
        },
        {
            "router": GetUser(),
            "path": "/users",
            "dependencies": [get_current_user],
        },
        {
            "router": CreateUser(),
            "path": "/sign-up",
            "dependencies": [],
        },
        {
            "router": Test(),
            "path": "/test",
            "dependencies": [],
        },
        {
            "router": Login(),
            "path": "/login",
            "dependencies": [],
        },
    ]


def routing(app):
    route_map = get_route_map()
    for obj in route_map:
        dec_list = obj.get("dependencies", [])
        api = Api(app)
        api.add_resource(
            obj["router"], obj["path"], dependencies=[Depends(d) for d in dec_list]
        )


# def routing(app):
#     route_map = get_route_map()
#     for obj in route_map:
#         dec_list = obj.get('decorators', [])
#         api = Api(app) if not dec_list else Api(app, dependencies=[Depends(d) for d in dec_list])
#         api.add_resource(obj['router'], obj['path'])

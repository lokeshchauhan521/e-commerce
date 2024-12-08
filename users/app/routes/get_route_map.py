from fastapi import Depends
from ..services.get_user import Get_user
from ..services.create_user import Create_user
from ..services.test import Test
from ..services.home import Home
from fastapi_utils import Api

def get_route_map():
    return [
        {
            "router": Home(),
            "path": "/",
            "dependencies": [],
        },
        {
            "router": Get_user(),
            "path": "/users",
            "dependencies": [],
        },
        {
            "router": Create_user(),
            "path": "/create-user",
            "dependencies": [],
        },
                {
            "router": Test(),
            "path": "/test",
            "dependencies": [],
        },
    ]

def routing(app):
    route_map = get_route_map()  
    for obj in route_map:
        dec_list = obj.get('decorators', [])
        api = Api(app) if not dec_list else Api(app, dependencies=[Depends(d) for d in dec_list])
        api.add_resource(obj['router'], obj['path'])
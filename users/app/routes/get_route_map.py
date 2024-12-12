from fastapi import Depends
from ..services.get_users import GetUsers
from ..services.auth.sign_up import SignUp
from ..services.home import Home
from ..services.auth.sign_in import SignIn
from fastapi_utils import Api

def get_route_map():
    return [
        {
            "router": Home(),
            "path": "/",
            "dependencies": [], 
        },
        {
            "router": GetUsers(),
            "path": "/users",
            "dependencies": [],
        },
        {
            "router": SignUp(),
            "path": "/sign-up",
            "dependencies": [],
        },
        {
            "router": SignIn(),
            "path": "/sign-in",
            "dependencies": [],
        }
    ]

def routing(app):
    route_map = get_route_map() 
    for obj in route_map:
        dec_list = obj.get("dependencies", [])
        api = Api(app)
        api.add_resource(obj["router"], obj["path"],dependencies=[Depends(d) for d in dec_list])

# def routing(app):
#     route_map = get_route_map()  
#     for obj in route_map:
#         dec_list = obj.get('decorators', [])
#         api = Api(app) if not dec_list else Api(app, dependencies=[Depends(d) for d in dec_list])
#         api.add_resource(obj['router'], obj['path'])
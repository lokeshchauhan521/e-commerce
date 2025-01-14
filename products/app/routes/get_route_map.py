from fastapi import Depends
from fastapi_utils import Api
from ..services.home import Home
from ..services.product.product import AddProduct , GetProduct
from ..services.category.add_category import AddCategory
secured_routes: list[str] = []


def get_route_map():
    return [
        {
            "router": Home(),
            "path": "/",
            "dependencies": [],
        },
        {
            "router": AddProduct(),
            "path": "/add-product",
            "dependencies": [],
        },
        {
            "router": AddCategory(),
            "path": "/add-category",
            "dependencies": [],
        },
        {
            "router": GetProduct(),
            "path": "/filter-product",
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
        if obj.get("requiredAuth") == True:
            secured_routes.append(obj["path"])



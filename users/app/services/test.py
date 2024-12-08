from fastapi_utils import Resource

class Test(Resource):
    def get(self):
        return {"fastapi":"fast api working fine"}
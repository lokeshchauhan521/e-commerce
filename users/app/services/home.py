from fastapi_utils import Resource


class Home(Resource):
    def get(self):
        return {"suceess": "application working fine "}

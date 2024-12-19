from app.core.utils.api_response import ResponseSuccess


class Home:
    def get(self):
        return ResponseSuccess("Product Server is up and running")

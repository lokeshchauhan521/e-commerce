from app.core.utils.api_response import ResponseSuccess


class Home:
    def get(self):
        return ResponseSuccess("Users Server is up and running")

from pydantic import BaseModel


class UserSignUp(BaseModel):
    email: str
    name: str
    password: str


class UserLogin(BaseModel):
    email: str
    password: str

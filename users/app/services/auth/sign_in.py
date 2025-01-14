from fastapi import Depends
from sqlalchemy.orm import Session
from app.models.user import User
from app.core.config.db import get_db
from app.core.utils.auth import verify_password
from app.core.utils.auth import create_access_token
from app.schemas.user import user as UserSchema
from app.core.utils.api_response import ResponseFailure, ResponseSuccess


class SignIn:
    def post(self, request: UserSchema.UserLogin, db: Session = Depends(get_db)):
        user = db.query(User).filter(User.email == request.email).first()
        print(user)
        if user is None or not verify_password(request.password, user.password):
            raise ResponseFailure(message="Invalid credentials")

        access_token = create_access_token(data={"email": user.email})
        return ResponseSuccess(
            message="Sign in successful",
            data={"access_token": access_token, "token_type": "bearer"},
        )

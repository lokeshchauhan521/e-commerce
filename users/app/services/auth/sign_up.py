from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status
from app.core.config.db import get_db
from app.core.utils.auth import hash_password
from app.core.utils.auth import create_access_token
from app.models.user import User
from app.schemas.user import user as UserSchema
from app.core.utils.api_response import ResponseFailure, ResponseSuccess


class SignUp:
    def post(self, request: UserSchema.UserSignUp, db: Session = Depends(get_db)):
        db_user = db.query(User).filter(User.email == request.email).first()
        if db_user:
            raise ResponseFailure("User already exists")
        hashed_password = hash_password(request.password)

        new_user = User(
            email=request.email,
            name=request.name,
            password=hashed_password,
        )

        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        access_token = create_access_token(data={"email": new_user.email})
        new_user.password = None
        return ResponseSuccess(
            "Account created successfylly",
            {"profile": new_user, "access_token": access_token},
            201,
        )

from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status
from app.core.config.db import get_db
from app.core.utils.auth import hash_password
from app.models.user import User
from app.schemas.user import user as UserSchema
from app.core.utils.responser import Responser


class SignUp:
    def post(self, request: UserSchema.UserSignUp, db: Session = Depends(get_db)):
        db_user = db.query(User).filter(User.email == request.email).first()
        data = {}
        if db_user:
            # return HTTPException(
            #     status_code=status.HTTP_400_BAD_REQUEST,
            #     detail="Email already registered",
            # )
            payload = Responser(data)
            return payload.response_400()

        hashed_password = hash_password(request.password)

        new_user = User(
            email=request.email,
            name=request.name,
            password=hashed_password,
        )

        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        data["email"] = new_user.email
        data["name"] = new_user.name
        # return {
        #     "message": "User created successfully",
        #     "user": {"email": new_user.email, "name": new_user.name},
        # }
        payload = Responser(data)
        return payload.response_201()

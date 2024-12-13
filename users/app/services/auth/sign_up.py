from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status
from app.core.config.db import get_db
from app.core.auth.security import hash_password
from app.models.user import User
from app.schemas.user import user as UserSchema
from app.core.responser.responser import Responser


class SignUp:
    async def post(self, request: UserSchema.UserSignUp, db: Session = Depends(get_db)):
                db_user = db.query(User).filter(User.email == request.email).first()
                data = {}
                if db_user:
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
                payload = Responser(data)
                return payload.response_201()
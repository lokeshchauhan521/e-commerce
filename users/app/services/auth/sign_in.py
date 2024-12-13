from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.user import User
from app.core.config.db import get_db
from app.core.auth.security import verify_password
from app.core.auth.security import create_access_token
from app.schemas.user import user as UserSchema
from app.core.responser.responser import Responser


class SignIn:
    async def post(self, request: UserSchema.UserLogin, db: Session = Depends(get_db)):
            user = db.query(User).filter(User.email == request.email).first()
            data = {}
            if user is None:
                payload = Responser(data)
                return payload.response_400()

            if not verify_password(request.password, user.password):
                payload = Responser(data)
                return payload.response_400()

            access_token = create_access_token(data={"sub": user.email})
            if access_token:
                data["token"] = access_token
            payload = Responser(data)
            return payload.response_200()

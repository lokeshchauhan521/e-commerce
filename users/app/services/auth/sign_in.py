from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.user import User
from app.core.config.db import get_db
from app.core.utils.auth import verify_password
from app.core.utils.auth import create_access_token
from app.schemas.user import user as UserSchema
from app.core.utils.exception_handler import CustomException


class SignIn:
    def post(self, request: UserSchema.UserLogin, db: Session = Depends(get_db)):
        raise CustomException("This is a custom error message", code=400)
        user = db.query(User).filter(User.email == request.email).first()
        if user is None or not verify_password(request.password, user.password):
            raise HTTPException(status_code=400, detail="Invalid credentials")

        access_token = create_access_token(data={"userEmail": user.email})
        return {"access_token": access_token, "token_type": "bearer"}

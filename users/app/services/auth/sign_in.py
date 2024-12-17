from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.user import User
from app.core.config.db import get_db
from app.core.utils.auth import verify_password
from app.core.utils.auth import create_access_token
from app.schemas.user import user as UserSchema


class SignIn:
    def post(self, request: UserSchema.UserLogin, db: Session = Depends(get_db)):

        user = db.query(User).filter(User.email == request.email).first()
        if user is None:
            raise HTTPException(status_code=400, detail="Invalid credentials")

        if not verify_password(request.password, user.password):
            raise HTTPException(status_code=400, detail="Invalid credentials")

        access_token = create_access_token(data={"userEmail": user.email})
        return {"access_token": access_token, "token_type": "bearer"}

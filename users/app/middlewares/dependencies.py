from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from app.core.utils.auth import decode_access_token
from app.core.config.db import get_db
from app.models.user import User
from app.core.utils.responser import Responser

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


async def get_current_user(token: str = Depends(oauth2_scheme), db=Depends(get_db)):
    data = {}
    payload = Responser(data)
    print(token)
    if token:
        token_data = decode_access_token(token)
        if token_data.email is None:
            return payload.response_400("Invalid Token")
        user_data = db.query(User).filter(User.email == token_data.email).first()
        if not user_data:
            payload.response_400("User not found")
        print("=============adadadad", data)
        return user_data
    else:
        return None

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.auth.dependencies import get_current_user
from app.core.config.db import get_db
from app.core.auth.security import decode_access_token 
from app.core.auth.dependencies import oauth2_scheme
from app.core.utils.responser.responser import Responser

class Profile:
    async def post(self, token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):     
        data = Responser()
        if token:
            token_data = decode_access_token(token)
            print("=================>",token_data)
        else:
            return data.response_400("Invalid token")      
              
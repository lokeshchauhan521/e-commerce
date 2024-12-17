from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.auth.dependencies import get_current_user
from app.core.config.db import get_db
from app.core.auth.security import decode_access_token 
from app.core.auth.dependencies import oauth2_scheme
from app.core.utils.responser.responser import Responser
from app.models.user import User 
class Profile:
    async def post(self, token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
        User = get_current_user()
        payload =  Responser()
        if User is None:
            return payload.response_400("Invalid token")
        
        return 
            
        # data  = {}
        # payload = Responser()
        # user_data = get_current_user(token)
        # print("========d14141414======>",data)
        # data["user_profile"] = {
        #     "email" : user_data.email,
        #     "name" : user_data.name
        # }
        # return payload.response_200()   
        # data = {}
        # payload = Responser(data)
        # if token:
        #     token_data = decode_access_token(token)
        #     print("=======2525252=========acca>a",token_data)
        #     if token_data.userEmail is None:
        #         return payload.response_400("Invalid Token")
        #     user_data = db.query(User).filter(User.email==token_data.userEmail).first()
        #     if not user_data:
        #         payload.response_400("User not found")
        #     data["user_profile"] = {
        #         "email" : user_data.email,
        #         "name" : user_data.name
        #     }
        #     return payload.response_200()
        # else:
        #     return payload.response_400("Invalid token")
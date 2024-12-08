from sqlalchemy.orm import Session
from fastapi import Depends
from ..models import user as UserModel
from ..db.get_db import get_db
from ..models import user as UserModel
from ..schemas import user as UserSchema
from fastapi_utils import Resource


class  Create_user(Resource):
    def post(self,request: UserSchema.User, db: Session = Depends(get_db) ):    
        new_user = UserModel.User(email = request.email, name = request.name)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
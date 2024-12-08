from sqlalchemy.orm import Session
from ..models import user as UserModel
from sqlalchemy.orm import Session
from ..db.get_db import get_db
from fastapi import Depends
from fastapi_utils import Resource

class Get_user(Resource):
    def get(self,db: Session = Depends(get_db) ):    
        return db.query(UserModel.User).all()
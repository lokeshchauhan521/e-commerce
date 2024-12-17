from fastapi import Depends
from sqlalchemy.orm import Session
from app.core.config.db import get_db
from app.core.utils.responser import Responser
from ..models import user as UserModel


class GetUsers:
    def get(self, db: Session = Depends(get_db)):
        data = {}
        data["data"] = db.query(UserModel.User).all()
        if not data:
            payload = Responser(data)
            return payload.response_400()
        else:
            payload = Responser(data)
            return payload.response_200()

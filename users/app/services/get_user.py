from fastapi import Depends
from fastapi_utils import Resource
from sqlalchemy.orm import Session

from ..db.get_db import get_db
from ..models import user as UserModel


class GetUser(Resource):
    def get(self, db: Session = Depends(get_db)):
        return db.query(UserModel.User).all()

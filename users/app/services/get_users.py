from fastapi import Depends
from sqlalchemy.orm import Session
from app.core.config.db import get_db
from ..models import user as UserModel


class GetUsers:
    def get(self, db: Session = Depends(get_db)):
        return db.query(UserModel.User).all()

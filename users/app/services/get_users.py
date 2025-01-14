from fastapi import Depends
from sqlalchemy.orm import Session
from app.core.config.db import get_db
from app.core.utils.api_response import ResponseSuccess
from ..models import user as UserModel


class GetUsers:
    def get(self, db: Session = Depends(get_db)):
        data = db.query(UserModel.User).all()
        return ResponseSuccess("Users fetched successfully", data)

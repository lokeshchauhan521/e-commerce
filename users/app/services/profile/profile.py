from fastapi import Depends, Request
from sqlalchemy.orm import Session
from app.core.config.db import get_db
from app.core.utils.api_response import ResponseSuccess


class Profile:
    async def get(self, request: Request, db: Session = Depends(get_db)):
        return ResponseSuccess("Profile fetched successfully", data=request.state.user)

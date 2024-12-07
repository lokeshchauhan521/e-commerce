from sqlalchemy import Column, Integer, String
from app.core.config.db import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    email=Column(String)
    name=Column(String)
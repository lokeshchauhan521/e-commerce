from sqlalchemy import Column, Integer, String
from app.core.config.db import Base

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, index=True)
    

    
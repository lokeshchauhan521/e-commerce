from sqlalchemy import Column, Integer, String, Float, Text, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship
from datetime import datetime
from ..core.config.db import Base

class Product(Base):
    __tablename__ = 'products'

    product_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    stock = Column(Integer, default=0, nullable=False)
    price = Column(Float, nullable=False)
    rating = Column(Float, nullable=True)
    created_at = Column(DateTime, default=datetime.timezone.utc, nullable=False)
    updated_at = Column(DateTime, default=datetime.timezone.utc, onupdate=datetime.timezone.utc, nullable=False)
    primary_image = Column(String)
    image_list = Column(String)
    brand = Column(String(255))
    # Relationships
    categories = relationship('Category', secondary='product_categories', back_populates='products')
    brand_id = Column(Integer, ForeignKey('brands.brand_id'), nullable=True)
    brand = relationship('Brand', back_populates='products')
    def __repr__(self):
        return f"<Product(name={self.name}, price={self.price}, stock={self.stock})>"



class Category(Base):
    __tablename__ = 'categories'

    category_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False, unique=True)

    products = relationship('Product', secondary=product_categories, back_populates='categories')

    def __repr__(self):
        return f"<Category(name={self.name})>"


class Brand(Base):
    __tablename__ = 'brands'

    brand_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False, unique=True)

    products = relationship('Product', back_populates='brand')

    def __repr__(self):
        return f"<Brand(name={self.name})>"

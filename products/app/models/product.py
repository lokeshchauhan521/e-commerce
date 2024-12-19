from sqlalchemy import Column, Integer, String, Float, Text, DateTime, ForeignKey, Table 
from sqlalchemy.orm import relationship
from datetime import datetime , timezone
from ..core.config.db import Base

# # Association table for many-to-many relationship between Product and Category
# product_categories = Table(
#     'product_categories',
#     Base.metadata,
#     Column('product_id', Integer, ForeignKey('products.product_id'), primary_key=True),
#     Column('category_id', Integer, ForeignKey('categories.category_id'), primary_key=True)
# )

class Product(Base):
    __tablename__ = 'products'

    product_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    stock = Column(Integer, default=0, nullable=False)
    price = Column(Float, nullable=False)
    rating = Column(Float, nullable=True)
    primary_image = Column(String(255), nullable=False)
    image_list= Column(String)
    brand = Column(String)
    created_at = Column(DateTime, default=datetime.now(timezone.utc), nullable=False)
    updated_at = Column(DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc), nullable=False)
   

    # Many-to-Many relationship with Category
    # categories = relationship('Category', secondary=product_categories, back_populates='products')

    def __repr__(self):
        return f"<Product(name={self.name}, price={self.price}, stock={self.stock})>"

# class Category(Base):
#     __tablename__ = 'categories'

#     category_id = Column(Integer, primary_key=True, autoincrement=True)
#     name = Column(String(255), nullable=False, unique=True)

#     # Many-to-Many relationship with Product
#     products = relationship('Product', secondary=product_categories, back_populates='categories')

#     def __repr__(self):
#         return f"<Category(name={self.name})>"

from fastapi import Depends
from sqlalchemy.orm import Session
from app.models.product import Product 
from app.core.config.db import get_db
from app.core.utils.api_response import ResponseSuccess, ResponseFailure
from app.schemas.product.product import ProductBase 
# from app.schemas.category.category import CategoryBase

class AddProduct:
    async def post(self, request: ProductBase, db: Session = Depends(get_db)):
        try:
            product_data = db.query(Product).filter(Product.name==request.name).first()

            if product_data:
                return ResponseFailure(message="Product already present",data={
                    "name" : product_data.name
                })
            product = Product(
                name=request.name,
                description=request.description,
                stock=request.stock,
                price=request.price,
                rating=request.rating,
                primary_image=request.primary_image,
                image_list=request.image_list,
                brand=request.brand
            )
            print("product values ", product)
            db.add(product)
            db.commit()
            db.refresh(product)
            return ResponseSuccess(message="Product added successfully", data={"product_id": product.product_id})
        except Exception as e:
            print("============>",e)
            raise ResponseFailure(message="failed", data={})
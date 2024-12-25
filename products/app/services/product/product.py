from fastapi import Depends
from sqlalchemy.orm import Session , joinedload 
from app.models.product import Product, Category
from app.core.config.db import get_db
from app.core.utils.api_response import ResponseSuccess, ResponseFailure
from app.schemas.product.product import ProductBase ,FilterProductBase

class AddProduct:
    async def post(self, request: ProductBase, db: Session = Depends(get_db)):
        try:
            product_data = db.query(Product).filter(Product.name == request.name).first()
            if product_data:
                return ResponseFailure(message="Product already present", data={
                    "name": product_data.name
                })

            category_objects = db.query(Category).filter(Category.name.in_(request.categories)).all()
            missing_categories = set(request.categories) - {category.name for category in category_objects}
            if missing_categories:
                return ResponseFailure(message="Unknow category", data={
                    "category": list(missing_categories)
                })

            product = Product(
                name=request.name,
                description=request.description,
                stock=request.stock,
                price=request.price,
                rating=request.rating,
                primary_image=request.primary_image,
                image_list=request.image_list,
                categories=category_objects 
            )

            print("product values:", product)
            db.add(product)
            db.commit()
            db.refresh(product)

            return ResponseSuccess(message="Product added successfully", data={"product_id": product.product_id})

        except Exception as e:
            raise ResponseFailure(message="failed", data={})
        
class GetProduct:
    async def post(self, request: FilterProductBase , db:Session = Depends(get_db)):
        try:
            query = db.query(Product).options(joinedload(Product.categories))

            '''
            The joinedload option eagerly loads the categories
            associated with the products, reducing database round-trips.
            '''
            if request.categories:
                query = query.filter(
                    Product.categories.any(Category.name.in_(request.categories))
                )

            products = query.all()

            result = [
                {
                    "product_id": product.product_id,
                    "name": product.name,
                    "description": product.description,
                    "stock": product.stock,
                    "price": product.price,
                    "rating": product.rating,
                    "primary_image": product.primary_image,
                    "categories": [category.name for category in product.categories],
                }
                for product in products
            ]

            return ResponseSuccess(message="success", data=result)

        except Exception as e:
            print(f"Error occurred: {e}")
            raise ResponseFailure(message="failed", data={})
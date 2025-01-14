from fastapi import Depends
from sqlalchemy.orm import Session
from app.models.product import Category
from app.core.config.db import get_db
from app.core.utils.api_response import ResponseSuccess, ResponseFailure
from app.schemas.category.category import  CategoryBase

class AddCategory:
    async def post(self, request: CategoryBase, db: Session = Depends(get_db)):
        data = request.categories
        try:
            existing_categories = (
                db.query(Category.name).all()
            )
            existing_category_names = {cat[0].lower() for cat in existing_categories}
            print("existing category ",existing_category_names)
            new_categories = [
                Category(name=cat)
                for cat in data
                if cat.lower() not in existing_category_names
            ]

            if new_categories:
                db.add_all(new_categories)
                db.commit()
            return ResponseSuccess(message="Categories added successfully", data={"category": data})
        except Exception as e:
            db.rollback()
            raise ResponseFailure(message="failed", data={})
from pydantic import BaseModel, Field
from typing import List, Optional

class ProductBase(BaseModel):
    name: str
    description: Optional[str]
    stock: int
    price: float
    rating: Optional[float]
    primary_image:str
    image_list :Optional[List[str]]
    brand : Optional[str]
    categories: List[str]


class FilterProductBase(BaseModel):
    categories: List[str] = None
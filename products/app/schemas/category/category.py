from pydantic import BaseModel
from typing import List

class CategoryBase(BaseModel):
    categories: List[str]
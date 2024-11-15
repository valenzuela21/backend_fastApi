from datetime import datetime
from pydantic import BaseModel
from typing import List

from src.schemas.productsChema import ProductOut

class CategoryCreate(BaseModel):
    name: str

    class Config:
        orm_mode = True

class CategoryOut(BaseModel):
    id: int
    name: str
    created_on: datetime
    updated_on: datetime
    products: List[ProductOut]

    class Config:
        orm_mode = True

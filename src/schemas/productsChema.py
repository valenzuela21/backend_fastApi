from datetime import datetime
from pydantic import BaseModel
from typing import Optional

from src.schemas.sharedChema import BrandOut, CategoryOut

class ProductCreate(BaseModel):
    name: str
    description: str
    category_id: int
    brand_id: int
    price: float
    rating: Optional[float] = None  # rating can be null

    class Config:
        from_attributes = True


class ProductOut(BaseModel):
    id: int
    name: str
    description: str
    price: float
    rating: Optional[float] = None
    brand: BrandOut
    category: CategoryOut
    created_on: datetime
    updated_on: datetime

    class Config:
        orm_mode = True

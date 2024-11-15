from datetime import datetime

from pydantic import BaseModel

class BrandCreate(BaseModel):
    name: str

    class Config:
        from_attributes = True

class BrandOut(BaseModel):
    id: int
    name: str
    created_on: datetime
    updated_on: datetime

    class Config:
        orm_mode = True

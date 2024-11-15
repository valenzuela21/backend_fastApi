from pydantic import BaseModel

class CategoryOut(BaseModel):
    id: int
    name: str
    class Config:
        orm_mode = True

class BrandOut(BaseModel):
    id: int
    name: str
    class Config:
        orm_mode = True


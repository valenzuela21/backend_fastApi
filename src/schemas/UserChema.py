from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class User(BaseModel):
    id: int
    full_name: str
    email: str
    password: str = ''
    role: Optional[str] = 'user'
    is_active: Optional[bool] = False
    created_on: Optional[datetime]
    updated_on: Optional[datetime]


class CreateUser(BaseModel):
    fullname: str
    email: str
    password: str

    class Config:
        json_schema_extra = {
            "example": {
                "fullname": "Abdulazeez Abdulazeez Adeshina",
                "email": "abdulazeez@x.com",
                "password": "weakpassword"
            }
        }


class UserLogin(BaseModel):
    username: str = Field(...)
    password: str = Field(...)

    class Config:
        json_schema_extra = {
            "example": {
                "username": "abdulazeez@x.com",
                "password": "weakpassword"
            }
        }

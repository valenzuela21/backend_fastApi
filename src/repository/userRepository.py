import base64
import os

from sqlalchemy.orm import Session
from src.utils import cryptoUtil
from src.models import User
from src.schemas.UserChema import CreateUser

def create(request: CreateUser, db: Session):
    new_user = User(
        full_name=request.fullname,
        email=request.email,
        password=cryptoUtil.get_hash(request.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user
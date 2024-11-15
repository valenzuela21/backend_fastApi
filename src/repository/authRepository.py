from fastapi import HTTPException, status
from src import models, schemas
from sqlalchemy.orm import Session
from sqlalchemy import and_

def find_existed_user(email: str, db: Session):

    user = db.query(models.User).filter(and_(models.User.email == email, models.User.is_active == True)).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Either user with email {email} not found OR currently in-active !")
    return user

## Checking if the JWT token is used before and the user is no longer active
def find_token_black_lists(token: str, db: Session):
    token = db.query(models.Blacklists).filter(models.Blacklists.token == token).first()
    return True if token else False
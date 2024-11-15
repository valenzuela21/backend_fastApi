from datetime import datetime, timezone
from fastapi import APIRouter, Depends, HTTPException, status, Body
from sqlalchemy.orm import Session
from src.models import User
from src.repository import userRepository
from src.schemas.UserChema import CreateUser, UserLogin
from src.utils import cryptoUtil, dbUtil

from src.utils.authHandlerUtil import sign_jwt

router = APIRouter(
    prefix="/auth",
    tags=["Auth"],
)

@router.post('/login')
def login_access_token(request: UserLogin = Body(...), db: Session = Depends(dbUtil.get_db)):
    user = db.query(User).filter(User.email == request.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Invalid Creadentials. !")

    if not cryptoUtil.verify(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Incorrect Password. !")

    ## Generate and return JWT token
    access_token = sign_jwt(request.username)
    db.query(User).filter(User.email == user.email).update(
        {
            User.is_active: True,
            User.updated_on: datetime.now(timezone.utc)
        }
    )
    db.commit()

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user_info": {
            "email": user.email,
            "fullname": user.full_name
        }
    }


@router.post("/register")
def register(request: CreateUser, db: Session = Depends(dbUtil.get_db)):
    ## To see if username/email exsist in Database
    usr = db.query(User).filter(User.email == request.email).first()

    if usr:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="User already registered. !")

    # Create new user
    return userRepository.create(request, db)
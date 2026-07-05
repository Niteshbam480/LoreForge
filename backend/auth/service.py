from sqlalchemy.orm import Session
from backend.auth.models import User
from fastapi import HTTPException
from backend.auth.schemas import UserCreate, LoginRequest, Token
from backend.core.security import hash_password, verify_password, create_access_token


def register_user(db: Session,data: UserCreate) -> User:
    existing_user = db.query(User).filter(User.email == data.email).first()
    if existing_user:
        raise HTTPException(status_code=400,detail="Email already registered")

    new_user =User(
        email=data.email,
        username=data.username,
        hashed_password=hash_password(data.password),
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user



def login_user(db: Session,data: LoginRequest) -> Token:
    user=db.query(User).filter(User.email == data.email).first()
    if not user or not verify_password(data.password,user.hashed_password):
        raise HTTPException(status_code=401,detail="Invalid credentials")
   
    token=create_access_token({"sub":user.email})
    return Token(access_token=token)


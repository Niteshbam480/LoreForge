from sqlalchemy.orm import Session
from backend.core.config import settings
from backend.auth.models import User
from backend.database.database import get_db
from datetime import timedelta, datetime, timezone
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from fastapi import Depends, HTTPException
from jose import jwt, JWTError



password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password) -> str:
    return password_context.hash(password)

def verify_password(password, hashed_password) -> bool:
    return password_context.verify(password, hashed_password)


def create_access_token(data: dict) -> str:
    payload= data
    payload["exp"] = datetime.now(timezone.utc) + timedelta(minutes=30)
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")
    return token


oauth_scheme=OAuth2PasswordBearer(tokenUrl="/auth/login")
def get_current_user(token:str=Depends(oauth_scheme),db:Session=Depends(get_db)):
    try:
        payload=jwt.decode(token,settings.SECRET_KEY,algorithms=["HS256"])
        email=payload.get("sub")
        if email is None:
            raise HTTPException(status_code=401,detail="could not validate credentials")
    except JWTError:
        raise HTTPException(status_code=401,detail="could not validate credentials")
    
    user=db.query(User).filter(User.email==email).first()
    if not user :
        raise HTTPException(status_code=401,detail="User not found")
    return user

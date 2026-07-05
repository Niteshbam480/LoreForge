from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import timedelta, datetime, timezone
from backend.core.config import settings



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
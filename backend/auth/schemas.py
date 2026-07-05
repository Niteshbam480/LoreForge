from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime


class UserCreate(BaseModel):
    email: str 
    username: str
    password: str = Field(min_length=8)

class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    email: str
    username: str
    created_at: datetime

class LoginRequest(BaseModel):
    email: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
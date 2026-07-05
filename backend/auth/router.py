from fastapi import APIRouter, Depends
from backend.database.database import get_db
from backend.auth.schemas import UserCreate, UserResponse, LoginRequest, Token
from backend.auth.service import register_user, login_user

router = APIRouter()

@router.post(
        "/register",
        response_model=UserResponse,
        status_code=201        
    )
def register(data:UserCreate, session = Depends(get_db)):
    return register_user(session,data)
    

@router.post("/login",response_model=Token)
def login(data: LoginRequest, session=Depends(get_db)):
    return login_user(session,data)




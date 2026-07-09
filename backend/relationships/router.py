from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.core.security import get_current_user
from backend.auth.models import User
from backend.database.database import get_db
from backend.relationships.schemas import RelationshipResponse, RelationshipCreate
from backend.relationships.service import create_relationship





router=APIRouter()


@router.post(
    "/",
    response_model=RelationshipResponse,
    status_code=201
)
def create(data:RelationshipCreate, db:Session=Depends(get_db),current_user:User=Depends(get_current_user)):
    return create_relationship(db,data,owner_id=current_user.id)
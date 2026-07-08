from sqlalchemy.orm import Session
from backend.auth.models import User
from backend.core.security import get_current_user
from fastapi import Depends, APIRouter
from backend.database.database import get_db
from backend.universes.schemas import UniverseResponse, UniverseCreate, UniverseUpdate, UniverseSummary
from backend.universes.service import get_universes,create_universe, get_universe, update_universe, delete_universe
from typing import List

router=APIRouter()


@router.get(
        "/",
        response_model=List[UniverseSummary])
def list_all_universes(db:Session=Depends(get_db),current_user: User =Depends(get_current_user)):
    return get_universes(db=db,owner_id=current_user.id)


@router.post(
        "/",
        response_model=UniverseResponse,
        status_code=201)
def create(data:UniverseCreate, db:Session=Depends(get_db),current_user: User =Depends(get_current_user)):
    return create_universe(db=db,data=data,owner_id=current_user.id)


@router.get(
        "/{universe_id}",
        response_model=UniverseResponse
        )
def universe(universe_id:int,db:Session=Depends(get_db),current_user:User=Depends(get_current_user)):
    return get_universe(db=db,universe_id=universe_id,owner_id=current_user.id)


@router.put(
    "/{universe_id}",
    response_model=UniverseResponse
    )
def update(universe_id:int,data:UniverseUpdate,db:Session=Depends(get_db),current_user:User=Depends(get_current_user)):
    return update_universe(db=db,universe_id=universe_id,data=data,owner_id=current_user.id)


@router.delete(
    "/{universe_id}",
    response_model=dict
)
def delete(universe_id:int,db:Session=Depends(get_db),current_user:User=Depends(get_current_user)):
    return delete_universe(db=db,universe_id=universe_id,owner_id=current_user.id)
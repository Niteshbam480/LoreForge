from sqlalchemy.orm import Session
from backend.universes.models import Universe
from backend.universes.schemas import UniverseCreate, UniverseUpdate
from fastapi import HTTPException


def get_universes(db:Session, owner_id:int):
    return db.query(Universe).filter(Universe.owner_id==owner_id).all()


def get_universe(db:Session, universe_id:int, owner_id:int):
    data = db.query(Universe).filter(Universe.id==universe_id, Universe.owner_id == owner_id).first()
    if not data:
        raise HTTPException(status_code=404,detail="Universe not found")
    return data


def create_universe(db:Session, data:UniverseCreate, owner_id:int):
        new_universe=Universe(
            name=data.name,
            description=data.description,
            is_public=data.is_public,
            owner_id=owner_id,
        )
        db.add(new_universe)
        db.commit()
        db.refresh(new_universe)
        return new_universe


def update_universe(db:Session, universe_id, data: UniverseUpdate, owner_id):
    universe=get_universe(db,universe_id,owner_id)
    updated_data=data.model_dump(exclude_unset=True)
    for key,value in updated_data.items():
         setattr(universe, key, value)
    db.commit()
    return get_universe(db,universe_id,owner_id)


def delete_universe(db:Session, universe_id:int,owner_id:int):
    universe=get_universe(db,universe_id,owner_id)
    db.delete(universe)
    db.commit()
    return {"message": "Universe deleted"}

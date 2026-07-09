from backend.relationships.models import Relationship
from backend.universes.models import Universe
from backend.nodes.models import Node
from backend.relationships.schemas import RelationshipCreate
from sqlalchemy.orm import Session
from fastapi import HTTPException



def create_relationship(db:Session, data:RelationshipCreate, owner_id:int):
    universe_id = data.universe_id
    source_node_id=data.source_node_id
    target_node_id=data.target_node_id
    universe = db.query(Universe).filter(Universe.id==universe_id, Universe.owner_id==owner_id ).first()
    if not universe:
        raise HTTPException(status_code=404,detail="Universe not found")
    source_node = db.query(Node).filter(Node.id==source_node_id).first()
    target_node = db.query(Node).filter(Node.id==target_node_id).first()
    if not source_node or not target_node:
        raise HTTPException(status_code=404,detail="Node not found")
    
    new_relationship=Relationship(
        source_node_id=source_node_id,
        target_node_id=target_node_id,
        rel_type=data.rel_type,
        universe_id=universe_id
    )
    db.add(new_relationship)
    db.commit()
    db.refresh(new_relationship)
    return new_relationship



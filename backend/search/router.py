from fastapi import APIRouter, Depends
from backend.auth.models import User
from backend.nodes.models import Node
from backend.universes.models import Universe
from backend.core.security import get_current_user
from backend.database.database import get_db
from sqlalchemy.orm import Session


router=APIRouter()


@router.get("/search")
def search(q:str,db:Session=Depends(get_db),current_user:User=Depends(get_current_user)):
    universe= db.query(Universe.id,Universe.name,Universe.is_public).filter(Universe.name.ilike(f"%{q}%")).all()
    node= db.query(Node.id,Node.name,Node.node_type).filter(Node.name.ilike(f"%{q}%")).all()
    universes_list = [{"id": u.id, "name": u.name, "is_public": u.is_public} for u in universe]
    nodes_list = [{"id": n.id, "name": n.name, "node_type": n.node_type} for n in node]
    return {"universes": universes_list, "nodes": nodes_list}
        
    


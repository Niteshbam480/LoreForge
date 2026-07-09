from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.auth.models import User
from backend.core.security import get_current_user
from backend.database.database import get_db
from backend.nodes.schemas import NodeResponse, NodeCreate, NodeSummary, NodeWithChildren
from backend.nodes.service import create_node, get_node, get_node_children, get_universe_nodes
from typing import List



router = APIRouter()

@router.post(
        "/",
        response_model=NodeResponse,
        status_code=201
    )
def create(data:NodeCreate, db:Session=Depends(get_db),current_user:User=Depends(get_current_user)):
    return create_node(db,data,owner_id=current_user.id)


@router.get("/{node_id}", response_model=NodeResponse)
def node(node_id:int, db:Session=Depends(get_db),current_user:User=Depends(get_current_user)):
    return get_node(db,node_id)


@router.get("/{node_id}/children",response_model=NodeWithChildren)
def children(node_id:int,db:Session=Depends(get_db),current_user:User=Depends(get_current_user)):
    return get_node_children(db,node_id)


@router.get("/universe/{universe_id}",response_model=List[NodeSummary])
def universe_node(universe_id:int,db:Session=Depends(get_db),current_user:User=Depends(get_current_user)):
    return get_universe_nodes(db,universe_id)
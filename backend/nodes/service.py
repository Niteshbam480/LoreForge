from backend.nodes.schemas import NodeCreate, ChildNode, NodeWithChildren
from backend.universes.models import Universe
from backend.nodes.models import Node
from backend.relationships.models import Relationship
from sqlalchemy.orm import Session
from fastapi import HTTPException




def create_node(db:Session,data:NodeCreate,owner_id:int):
    universe_id=data.universe_id
    universe=db.query(Universe).filter(Universe.owner_id==owner_id, Universe.id==universe_id).first()
    if not universe:
        raise HTTPException(status_code=404,detail="Universe not found")
    
    new_node=Node(
        name=data.name,
        node_type=data.node_type,
        properties=data.properties,
        universe_id=universe_id
    )

    db.add(new_node)
    db.commit()
    db.refresh(new_node)
    return new_node


def get_node(db:Session,node_id:int):
    node = db.query(Node).filter(Node.id==node_id).first()
    if not node:
        raise HTTPException(status_code=404,detail="Node not found")
    return node


def get_node_children(db:Session,node_id:int):
    node = get_node(db,node_id)
    relationships=db.query(Relationship).filter(Relationship.source_node_id == node_id).all()
    children=[]
    for relationship in relationships:
        child = get_node(db,relationship.target_node_id)
        children.append(
            ChildNode(
                id=child.id,
                name=child.name,
                node_type=child.node_type,
                rel_type=relationship.rel_type,
                ))

    return NodeWithChildren(
        id=node.id,
        name=node.name,
        node_type=node.node_type,
        children=children,
    )


def get_universe_nodes(db:Session,universe_id:int):
    return db.query(Node).filter(Node.universe_id==universe_id).all()

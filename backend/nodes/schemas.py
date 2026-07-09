from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime
from enum import Enum




class NodeType(str,Enum):
    character="character"
    location = "location"
    event = "event"
    organization = "organization"
    artifact = "artifact"
    species = "species"
    timeline = "timeline"


class NodeCreate(BaseModel):
    name: str
    node_type: NodeType
    properties: dict = Field(default_factory=dict)
    universe_id: int


class NodeResponse(BaseModel):
    model_config=ConfigDict(from_attributes=True)

    id:int
    name:str
    node_type:NodeType
    properties: dict
    universe_id:int
    created_at:datetime


class NodeSummary(BaseModel):
    model_config=ConfigDict(from_attributes=True)

    id:int
    name:str
    node_type:NodeType


class ChildNode(BaseModel):
    model_config=ConfigDict(from_attributes=True)

    id:int
    name:str
    node_type:NodeType
    rel_type:str


class NodeWithChildren(BaseModel):
    model_config=ConfigDict(from_attributes=True)

    id:int
    name:str
    node_type:NodeType
    children:list[ChildNode]

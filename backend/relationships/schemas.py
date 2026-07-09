from pydantic import BaseModel, ConfigDict, model_validator
from datetime import datetime



class RelationshipCreate(BaseModel):
    source_node_id:int
    target_node_id:int
    rel_type:str
    universe_id:int

    @model_validator(mode="after")
    def validate_nodes(self):
        if self.source_node_id == self.target_node_id:
            raise ValueError("Source Node and Target Node cannot be same")
        return self
    

class RelationshipResponse(BaseModel):
    model_config=ConfigDict(from_attributes=True)

    id:int
    source_node_id:int
    target_node_id:int
    rel_type:str
    universe_id:int
    created_at:datetime
from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime


class UniverseCreate(BaseModel):
    name: str
    description: str|None = None
    is_public: bool = Field(default=True)


class UniverseUpdate(BaseModel):
    name: str|None = None
    description: str|None = None
    is_public: bool|None  = None

class UniverseResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
    description: str|None=None
    is_public: bool
    owner_id: int
    created_at: datetime

class UniverseSummary(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    name: str
    is_public: bool




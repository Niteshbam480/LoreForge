from sqlalchemy import Column, Integer, String, DateTime, JSON, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from backend.database.database import Base


class Node(Base):
    __tablename__ = "nodes"

    id = Column(Integer,primary_key=True)
    name = Column(String,nullable=False)
    node_type = Column(String,nullable=False)
    properties = Column(JSON,default=dict)
    universe_id = Column(Integer,ForeignKey("universes.id"))
    created_at = Column(DateTime,default=datetime.now(timezone.utc))
    universe = relationship("Universe", back_populates="nodes")
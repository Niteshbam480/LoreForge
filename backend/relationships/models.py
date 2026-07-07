from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from backend.database.database import Base


class Relationship(Base):
    __tablename__="relationships"

    id = Column(Integer,primary_key=True)
    source_node_id = Column(Integer,ForeignKey("nodes.id"),nullable=False)
    target_node_id = Column(Integer,ForeignKey("nodes.id"),nullable=False)
    rel_type = Column(String,nullable=False)
    universe_id = Column(Integer,ForeignKey("universes.id"))
    created_at = Column(DateTime,default=datetime.now(timezone.utc))

    source_node=relationship("Node",foreign_keys=[source_node_id])
    target_node=relationship("Node",foreign_keys=[target_node_id])
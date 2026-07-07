from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from backend.database.database import Base


class Universe(Base):
    __tablename__ = "universes"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String,nullable=True)
    is_public=Column(Boolean,default=True)
    owner_id=Column(Integer,ForeignKey("users.id"))
    created_at=Column(DateTime,default=datetime.now(timezone.utc))
    owner=relationship("User", back_populates="universes")
    nodes=relationship("Node", back_populates="universe", cascade="all, delete-orphan")
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from backend.database.database import Base




class User(Base):
    __tablename__ = "users"
    
    
    id = Column(Integer,primary_key=True)
    email = Column(String,unique=True,nullable=False)
    username = Column(String,unique=True,nullable=False)
    hashed_password = Column(String,nullable=False)
    created_at = Column(DateTime,default=datetime.now(timezone.utc))
    is_active = Column(Boolean,default=True)
    universes = relationship("Universe", back_populates="owner", cascade=("all, delete-orphan"))
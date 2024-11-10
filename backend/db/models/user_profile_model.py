# db/models/user_profile_model.py
from sqlalchemy import Column, Integer, String, JSON, DateTime, ForeignKey
from sqlalchemy.sql import func
from db.database import Base

class UserProfile(Base):
    __tablename__ = 'user_profile'

    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    name = Column(String(100))
    age = Column(Integer)
    preferences = Column(JSON)
    dietary_restrictions = Column(JSON)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    
    user = relationship("User", back_populates="profile")

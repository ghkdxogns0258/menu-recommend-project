from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from db.database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    provider_id = Column(String(100), unique=True, nullable=False)  # 소셜 로그인 고유 ID
    provider = Column(String(50), nullable=False)                   # 로그인 제공자 이름
    email = Column(String(100), unique=True)
    created_at = Column(DateTime, default=func.now())

    profile = relationship("UserProfile", back_populates="user", uselist=False)

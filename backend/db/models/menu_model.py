# db/models/menu_model.py
from sqlalchemy import Column, Integer, String, JSON, DateTime
from sqlalchemy.sql import func
from db.database import Base

class Menu(Base):
    __tablename__ = 'menus'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    description = Column(String)
    cuisine_type = Column(String(50))
    taste_profile = Column(JSON)  # JSON 필드를 사용해 다양한 맛 프로필 저장
    created_at = Column(DateTime, default=func.now())
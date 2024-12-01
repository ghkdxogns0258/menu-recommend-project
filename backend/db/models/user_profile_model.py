from sqlalchemy import Column, Integer, String, JSON, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from db.database import Base

class UserProfile(Base):
    __tablename__ = 'user_profile'

    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    name = Column(String(100))
    age = Column(Integer)
    preferences = Column(JSON)               # 선호도 정보
    user_taste_profile = Column(JSON)             # 입맛 정보
    recent_menus = Column(JSON, default={})  # 최근 선택 메뉴
    is_info_complete = Column(Boolean, default=False)  # 정보 입력 완료 여부
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())  # 자동 갱신

    user = relationship("User", back_populates="profile")
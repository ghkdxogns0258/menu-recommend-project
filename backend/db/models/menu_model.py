from sqlalchemy import Column, Integer, String, JSON, DateTime, Boolean
from sqlalchemy.sql import func
from db.database import Base

class Menu(Base):
    __tablename__ = 'menus'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)  # 메뉴 이름
    description = Column(String)                # 메뉴 설명
    cuisine_type = Column(String(50))           # 요리 스타일
    menu_features = Column(JSON, nullable=False)  
    time_morning = Column(Boolean, default=False)  # 아침 적합성
    time_lunch = Column(Boolean, default=False)    # 점심 적합성
    time_dinner = Column(Boolean, default=False)   # 저녁 적합성
    weather_cold = Column(Boolean, default=False)  # 추운 날 적합성
    weather_hot = Column(Boolean, default=False)   # 더운 날 적합성
    weather_rainy = Column(Boolean, default=False) # 비 오는 날 적합성
    created_at = Column(DateTime, default=func.now())
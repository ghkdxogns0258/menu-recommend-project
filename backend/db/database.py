# db/database.py
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('USER_DB_NAME')}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 모든 모델에서 상속받을 Base 클래스
Base = declarative_base()

def initialize_db():
    """모든 테이블 생성"""
    from db.models.user_model import User
    from db.models.user_profile_model import UserProfile
    from db.models.menu_model import Menu
    Base.metadata.create_all(bind=engine)

def get_connection(db_name):
    """데이터베이스 연결 설정"""
    db_url = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{db_name}"
    return create_engine(db_url)
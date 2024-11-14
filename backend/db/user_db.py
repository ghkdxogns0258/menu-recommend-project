# db/user_db.py

from db.database import SessionLocal
from db.models.user_model import User
from db.models.user_profile_model import UserProfile

def create_user(provider_id, provider):
    """user_auth_db에 사용자 추가"""
    with SessionLocal() as session:
        new_user = User(provider_id=provider_id, provider=provider)
        session.add(new_user)
        session.commit()
        session.refresh(new_user)
        return new_user.id

def get_user_by_provider_id(provider_id):
    """provider_id로 사용자 정보 조회"""
    with SessionLocal() as session:
        user = session.query(User).filter(User.provider_id == provider_id).first()
        return user

def get_user_profile(user_id):
    """user_profile 테이블에서 사용자 정보 조회"""
    with SessionLocal() as session:
        user_profile = session.query(UserProfile).filter(UserProfile.user_id == user_id).first()
        return user_profile

def update_user_info_complete(user_id):
    """사용자 정보 입력 완료 상태를 True로 업데이트"""
    with SessionLocal() as session:
        user_profile = session.query(UserProfile).filter(UserProfile.user_id == user_id).first()
        if user_profile:
            user_profile.is_info_complete = True
            session.commit()

def update_user_preferences(user_id, preferences):
    """사용자 선호도를 업데이트합니다."""
    with SessionLocal() as session:
        try:
            user_profile = session.query(UserProfile).filter(UserProfile.user_id == user_id).first()
            if not user_profile:
                # user_profile이 없으면 생성
                user_profile = UserProfile(user_id=user_id)
                session.add(user_profile)
                session.commit()

            user_profile.preferences = preferences
            session.commit()
            print(f"Preferences updated successfully for user_id {user_id}")  # 로그 추가
        except Exception as e:
            session.rollback()  # 트랜잭션 롤백
            print("Error updating preferences:", e)  # 예외 메시지 로그
            return {"error": str(e)}, 500  # 예외 메시지를 클라이언트에 반환

def update_user_tastes(user_id, tastes):
    """사용자 입맛 정보를 업데이트합니다."""
    with SessionLocal() as session:
        try:
            user_profile = session.query(UserProfile).filter(UserProfile.user_id == user_id).first()
            if not user_profile:
                # user_profile이 없으면 생성
                user_profile = UserProfile(user_id=user_id)
                session.add(user_profile)
                session.commit()

            # taste_profile에 tastes 객체를 그대로 할당
            user_profile.taste_profile = tastes
            user_profile.is_info_complete = True

            session.commit()
            print(f"Taste profile updated successfully for user_id {user_id}")  # 로그 추가
            return {"message": "Taste profile updated successfully"}, 200
        except Exception as e:
            session.rollback()  # 트랜잭션 롤백
            print("Error updating taste profile:", e)  # 예외 메시지 로그
            return {"error": str(e)}, 500  # 예외 메시지를 클라이언트에 반환

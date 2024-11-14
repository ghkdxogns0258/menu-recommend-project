# utils/user_utils.py

from db.database import SessionLocal
from db.models.user_profile_model import UserProfile

def save_user_preferences(user_id, preferences, dietary_restrictions):
    """사용자의 선호도 및 식이 제한 정보를 저장"""
    with SessionLocal() as session:
        # user_id로 UserProfile을 조회합니다.
        profile = session.query(UserProfile).filter(UserProfile.user_id == user_id).first()
        
        # 프로필이 이미 있으면 업데이트, 없으면 새로 생성
        if profile:
            profile.preferences = preferences
            profile.dietary_restrictions = dietary_restrictions
        else:
            profile = UserProfile(
                user_id=user_id,
                preferences=preferences,
                dietary_restrictions=dietary_restrictions
            )
            session.add(profile)
        
        # 변경 사항을 데이터베이스에 커밋
        session.commit()

def get_user_preferences(user_id):
    """사용자의 선호도 및 식이 제한 정보를 가져오기"""
    with SessionLocal() as session:
        profile = session.query(UserProfile).filter(UserProfile.user_id == user_id).first()
        if profile:
            return {
                "preferences": profile.preferences,
                "dietary_restrictions": profile.dietary_restrictions
            }
        return None
from db.database import SessionLocal
from db.models.user_model import User
from db.models.user_profile_model import UserProfile
from utils.logging.logger import logger

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
        user_profile = session.query(UserProfile).filter(UserProfile.user_id == user_id).first()

        # user_profile이 없으면 생성
        if not user_profile:
            user_profile = UserProfile(user_id=user_id, preferences=preferences)
            session.add(user_profile)
        else:
            user_profile.preferences = preferences  # 선호도 업데이트

        session.commit()
        print(f"Preferences updated successfully for user_id {user_id}")

def update_user_tastes(user_id, tastes):
    """
    사용자 입맛 정보를 업데이트합니다.
    Args:
        user_id (int): 사용자 ID.
        tastes (dict): 사용자의 입맛 정보.
    Returns:
        dict: 처리 결과 메시지와 상태 코드.
    """
    try:
        logger.debug(f"Starting update_user_tastes for user_id={user_id} with tastes={tastes}")
        
        with SessionLocal() as session:
            # 사용자 프로필 검색
            user_profile = session.query(UserProfile).filter(UserProfile.user_id == user_id).first()
            logger.debug(f"User profile found: {user_profile}")

            # user_profile이 없으면 생성
            if not user_profile:
                logger.info(f"No user profile found for user_id={user_id}. Creating a new profile.")
                user_profile = UserProfile(user_id=user_id, user_taste_profile=tastes, is_info_complete=True)
                session.add(user_profile)
            else:
                logger.info(f"Updating user_taste_profile for user_id={user_id}")
                user_profile.user_taste_profile = tastes  # 입맛 정보 업데이트
                user_profile.is_info_complete = True

            # 변경사항 저장
            session.commit()
            logger.info(f"Taste profile successfully updated for user_id={user_id}")

            return {"message": "Taste profile updated successfully"}, 200

    except Exception as e:
        logger.error(f"Error updating taste profile for user_id={user_id}: {e}", exc_info=True)
        return {"error": "Internal server error"}, 500


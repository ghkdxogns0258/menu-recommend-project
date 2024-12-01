from db.database import SessionLocal
from db.models.user_profile_model import UserProfile
from utils.model_initializer import initialize_user_model  # 모델 초기화 유틸 추가


def save_user_preferences(user_id, preferences):
    """
    사용자의 선호도 정보를 저장합니다.
    - `preferences`: 사용자가 입력한 선호도 데이터 (예: {"taste": 0.5, "value": 0.75, ...}).
    """
    with SessionLocal() as session:
        # user_id로 UserProfile 조회
        profile = session.query(UserProfile).filter(UserProfile.user_id == user_id).first()

        if profile:
            # 기존 프로필이 있으면 선호도 정보 업데이트
            profile.preferences = preferences
        else:
            # 기존 프로필이 없으면 새로 생성
            profile = UserProfile(
                user_id=user_id,
                preferences=preferences
            )
            session.add(profile)

        # 변경 사항 DB에 저장
        session.commit()
        print(f"Preferences saved for user_id {user_id}")


def save_user_taste_profile(user_id, taste_profile):
    """
    사용자의 입맛 정보를 저장하고 모델을 초기화합니다.
    """
    with SessionLocal() as session:
        # user_id로 UserProfile 조회
        profile = session.query(UserProfile).filter(UserProfile.user_id == user_id).first()

        if profile:
            # 기존 프로필이 있으면 입맛 정보 업데이트
            profile.user_taste_profile = taste_profile
            profile.is_info_complete = True  # 정보 입력 완료 상태
        else:
            # 기존 프로필이 없으면 새로 생성
            profile = UserProfile(
                user_id=user_id,
                user_taste_profile=taste_profile,
                is_info_complete=True
            )
            session.add(profile)

        # 변경 사항 DB에 저장
        session.commit()
        print(f"Taste profile saved for user_id {user_id}")

    # 입맛 정보 입력 완료 후 모델 초기화 호출
    try:
        initialize_user_model(user_id)
    except Exception as e:
        print(f"Failed to initialize model for user_id {user_id}: {e}")


def get_user_preferences(user_id):
    """
    사용자의 선호도 및 입맛 정보를 반환합니다.
    - 반환값: {"preferences": {...}, "user_taste_profile": {...}}
    """
    with SessionLocal() as session:
        profile = session.query(UserProfile).filter(UserProfile.user_id == user_id).first()
        if profile:
            return {
                "preferences": profile.preferences,  # 선호도 정보
                "user_taste_profile": profile.user_taste_profile,  # 입맛 정보
            }
        print(f"No user profile found for user_id {user_id}")
        return None

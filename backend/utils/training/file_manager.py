import os

def get_weights_path(user_id):
    """
    사용자별 모델 파일 경로 반환.
    """
    return os.path.join("logs", "weights", f"user_{user_id}_weights.pth")

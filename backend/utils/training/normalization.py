# utils/training/normalization.py
import numpy as np

def normalize_features(features):
    """
    최소-최대 정규화 함수:
    - 딕셔너리 또는 리스트 데이터 지원.
    - 문자열 데이터를 float으로 변환 후 처리.
    - 잘못된 데이터 타입을 검출하여 에러를 반환.
    """
    try:
        if isinstance(features, dict):
            # 값이 문자열인 경우 float으로 변환
            converted_features = {k: float(v) for k, v in features.items()}
            max_val = max(converted_features.values())
            min_val = min(converted_features.values())
            if max_val == min_val:  # 모든 값이 동일한 경우
                return converted_features  # 정규화하지 않고 그대로 반환
            return {k: (v - min_val) / (max_val - min_val) for k, v in converted_features.items()}

        elif isinstance(features, list):
            # 문자열을 float으로 변환
            converted_features = [float(f) for f in features]
            max_val = max(converted_features)
            min_val = min(converted_features)
            if max_val == min_val:
                return converted_features
            return [(f - min_val) / (max_val - min_val) for f in converted_features]

        else:
            raise ValueError(f"Unsupported data type for normalization: {type(features)}")

    except (TypeError, ValueError) as e:
        raise ValueError(f"Invalid feature value in normalization: {features}. Error: {e}")




def normalize_user_preferences(preferences):
    """
    사용자 선호도 벡터 정규화 함수:
    - 0~1 범위가 아니면 자동 정규화 수행.
    """
    if isinstance(preferences, dict):
        return normalize_features(preferences)
    elif isinstance(preferences, list) and all(0 <= p <= 1 for p in preferences):
        return preferences  # 이미 정규화된 경우 그대로 반환
    else:
        return normalize_features(preferences)  # 정규화 수행


import numpy as np

# 특성을 0~1 범위로 정규화하는 함수 정의
def normalize_features(features):
    """
    특성 벡터를 정규화하여 0~1 사이의 값으로 변환하는 함수.
    
    Args:
        features (list): 원본 특성 벡터
    
    Returns:
        list: 정규화된 특성 벡터
    """
    # 특성 벡터의 최대값과 최소값 계산
    max_val = max(features)
    min_val = min(features)
    
    # 정규화 공식 적용
    normalized = [(f - min_val) / (max_val - min_val) for f in features]
    return normalized  # 정규화된 벡터 반환
# utils/data/normalization.py
import numpy as np

def normalize_features(features):
    max_val = max(features)
    min_val = min(features)
    return [(f - min_val) / (max_val - min_val) for f in features]

# 사용자 선호도 벡터 정규화 함수
def normalize_user_preferences(preferences):
    return normalize_features(preferences)
# utils/evaluation/metrics.py

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# 모델 평가 함수 정의
def evaluate_model(y_true, y_pred):
    """
    모델의 성능 평가 지표를 계산하는 함수.
    
    Args:
        y_true (list): 실제 레이블 리스트
        y_pred (list): 예측된 레이블 리스트
    
    Returns:
        dict: accuracy, precision, recall, f1-score 값을 포함하는 딕셔너리
    """
    # 각각의 평가 지표 계산
    return {
        "accuracy": accuracy_score(y_true, y_pred),  # 정확도 계산
        "precision": precision_score(y_true, y_pred),  # 정밀도 계산
        "recall": recall_score(y_true, y_pred),  # 재현율 계산
        "f1_score": f1_score(y_true, y_pred)  # F1 점수 계산
    }
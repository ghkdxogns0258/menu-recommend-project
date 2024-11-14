# train.py
import torch
import torch.nn as nn
import torch.optim as optim
from utils.logging.logger import logger
from utils.evaluation.metrics import evaluate_model
from utils.data.data_loader import load_menu_data
from model.recommendation_model import MenuRecommendationNet
from utils.monitoring.weight_logger import save_weights  # 가중치 저장 함수 호출

# 메뉴 데이터 로드
menu_data = load_menu_data()

# 모델 인스턴스 생성 (입력층 크기는 메뉴 특성 수와 동일)
model = MenuRecommendationNet(input_size=len(menu_data[0]['features']))

# 이진 교차 엔트로피 손실 함수 정의
criterion = nn.BCELoss()

# Adam 옵티마이저 생성, 학습률 0.01 설정
optimizer = optim.Adam(model.parameters(), lr=0.01)

# 피드백에 따른 모델 학습 함수 정의
def train_feedback(menu, liked, epoch, preferences, taste_profile):
    # 메뉴의 특성을 텐서로 변환
    features = torch.tensor(menu['features'], dtype=torch.float32)
    
    # 선호도와 입맛을 반영하여 초기 가중치를 설정
    model.initialize_weights(preferences, taste_profile)
    
    # 피드백을 레이블로 변환 (좋아요는 1, 싫어요는 0)
    label = torch.tensor([1.0 if liked else 0.0], dtype=torch.float32)
    
    optimizer.zero_grad()  # 이전 단계의 기울기 초기화
    output = model(features)  # 모델 출력 계산
    loss = criterion(output, label)  # 손실 계산
    loss.backward()  # 역전파로 기울기 계산
    optimizer.step()  # 파라미터 업데이트
    
    logger.info(f"Training loss at epoch {epoch}: {loss.item()}")  # 에포크 별 손실 값 로깅

    # 에포크 단위로 가중치 저장
    save_weights(model, epoch)
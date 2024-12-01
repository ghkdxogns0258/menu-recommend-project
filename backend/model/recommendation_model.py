# model/recommendation_model.py
import torch
import torch.nn as nn
import torch.nn.functional as F

class MenuRecommendationNet(nn.Module):
    """
    MenuRecommendationNet:
    사용자 선호도(5가지)와 입맛 정보(5가지), 외부 요인을 반영한 메뉴 추천 모델.
    - 선호도: 모델의 가중치 초기화에 반영.
    - 입맛 정보: 모델의 편향 초기화에 반영.
    """

    def __init__(self, input_size, num_menus):
        """
        네트워크 초기화:
        - input_size: 입력 특징 벡터의 크기 (taste_profile + 외부 요인).
        - num_menus: 추천 대상 메뉴의 총 개수 (소프트맥스 출력 크기).
        """
        super(MenuRecommendationNet, self).__init__()
        
        # 첫 번째 레이어: 입력에서 16차원으로 축소
        self.fc1 = nn.Linear(input_size, 16)
        
        # 두 번째 레이어: 중간 표현을 32차원으로 확장
        self.fc2 = nn.Linear(16, 32)
        
        # 세 번째 레이어: 32차원을 다시 16차원으로 축소
        self.fc3 = nn.Linear(32, 16)
        
        # 출력 레이어: 각 메뉴에 대한 점수를 출력
        self.output = nn.Linear(16, 1)  # 단일 출력 노드

    def forward(self, x):
        """
        순전파(Forward Pass):
        - 입력 x를 받아 신경망을 통과시킨 후 각 메뉴의 확률 분포를 반환.
        """
        # 첫 번째 레이어 + ReLU 활성화 함수
        x = torch.relu(self.fc1(x))
        
        # 두 번째 레이어 + ReLU 활성화 함수
        x = torch.relu(self.fc2(x))
        
        # 세 번째 레이어 + ReLU 활성화 함수
        x = torch.relu(self.fc3(x))
        
         # 출력 레이어 + Softmax 활성화 함수 (각 메뉴에 대한 확률 계산)
        x = self.output(x)
        return F.softmax(x, dim=1)  # 각 메뉴에 대한 확률 계산

    def initialize_weights(self, preferences, user_taste_profile):
        """
        가중치와 편향 초기화:
        - 선호도: 첫 번째 레이어(fc1)의 가중치에 반영.
        - 입맛 정보: 첫 번째 레이어(fc1)의 편향에 반영.
        """
        if len(preferences) != 5 or len(user_taste_profile) != 5:
            raise ValueError("Preferences and user_taste_profile should each have exactly 5 elements.")
        
        with torch.no_grad():  # 초기화 과정에서 그래디언트 비활성화
            # 가중치 초기화 (선호도 기반)
            for i, weight in enumerate(preferences):
                self.fc1.weight.data[i, :5] = torch.tensor(preferences, dtype=torch.float32)
            
            # 편향 초기화 (입맛 기반)
            self.fc1.bias.data[:5] = torch.tensor(user_taste_profile, dtype=torch.float32)

            print("Initialized weights and biases based on preferences and user_taste_profile.")
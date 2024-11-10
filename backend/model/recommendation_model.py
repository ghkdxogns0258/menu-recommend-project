import torch
import torch.nn as nn

# 신경망 모델 클래스 정의
class MenuRecommendationNet(nn.Module):
    def __init__(self, input_size):
        super(MenuRecommendationNet, self).__init__()
        # 첫 번째 은닉층 (입력 크기 -> 16개의 뉴런)
        self.fc1 = nn.Linear(input_size, 16)
        # 두 번째 은닉층 (16 -> 32개의 뉴런)
        self.fc2 = nn.Linear(16, 32)
        # 세 번째 은닉층 (32 -> 16개의 뉴런)
        self.fc3 = nn.Linear(32, 16)
        # 출력층 (16 -> 1개의 뉴런, 선호도 예측)
        self.output = nn.Linear(16, 1)

    def forward(self, x):
        x = torch.relu(self.fc1(x))  # 첫 번째 은닉층 + ReLU
        x = torch.relu(self.fc2(x))  # 두 번째 은닉층 + ReLU
        x = torch.relu(self.fc3(x))  # 세 번째 은닉층 + ReLU
        x = torch.sigmoid(self.output(x))  # 출력층 + Sigmoid (확률)
        return x
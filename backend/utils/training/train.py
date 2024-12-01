import os
import torch
import torch.nn as nn
import torch.optim as optim
from utils.logging.logger import logger
from utils.data.data_loader import load_menu_data
from utils.training.file_manager import get_weights_path
from utils.model_manager import ModelManager
from model.recommendation_model import MenuRecommendationNet

# 메뉴 데이터 로드 및 검증
menu_data = load_menu_data()
if not menu_data or "menu_features" not in menu_data[0]:
    logger.error("Invalid menu_data: 'menu_features' key is missing or data is empty.")
    raise ValueError("Invalid menu_data: 'menu_features' key is missing or data is empty.")

logger.info(f"Loaded menu_data with {len(menu_data)} items.")

# 손실 함수 정의
criterion = nn.CrossEntropyLoss()

# 모델 초기화
input_size = 11  # menu_features (5) + external_factors (6)
num_menus = len(menu_data)
model = MenuRecommendationNet(input_size=input_size, num_menus=num_menus)
logger.info(f"Initialized MenuRecommendationNet with input_size={input_size}, num_menus={num_menus}")

# 옵티마이저 정의
optimizer = optim.Adam(model.parameters(), lr=0.01)
logger.info("Optimizer and loss function initialized.")

model_manager = ModelManager(input_size=11, num_menus=len(menu_data))


def save_training_state(user_id, epoch, model, optimizer):
    """
    사용자별 학습된 모델 상태를 저장합니다.
    """
    weights_path = get_weights_path(user_id)
    checkpoint = {
        "model_state_dict": model.state_dict(),
        "optimizer_state_dict": optimizer.state_dict(),
        "epoch": epoch,
        "learning_rate": optimizer.param_groups[0]["lr"],
    }

    os.makedirs(os.path.dirname(weights_path), exist_ok=True)
    torch.save(checkpoint, weights_path)
    logger.info(f"Training state for user {user_id} saved at {weights_path}.")


def train_feedback(menu, liked, user_id, epoch):
    """
    사용자 피드백 기반 학습.
    """
    logger.debug(f"Training started for menu: {menu.get('name', 'Unknown')} at epoch {epoch}")
    with model_manager.get_lock(user_id):
        model = model_manager.get_model(user_id)
        optimizer = model_manager.get_optimizer(user_id)  # 기존 옵티마이저 사용

        try:
            # 메뉴 특징 벡터와 외부 요인 생성
            menu_features_vector = list(menu["menu_features"].values())
            external_factors = [
                int(menu["time_morning"]),
                int(menu["time_lunch"]),
                int(menu["time_dinner"]),
                int(menu["weather_cold"]),
                int(menu["weather_hot"]),
                int(menu["weather_rainy"]),
            ]
            combined_features = menu_features_vector + external_factors

            # 입력 데이터 텐서 생성
            features = torch.tensor(combined_features, dtype=torch.float32).unsqueeze(0)
            label = torch.tensor([1 if liked else 0], dtype=torch.long)
            print("Training feedback:")
            print("Features:", features.tolist())
            print("Label:", label.tolist())
            # 모델 학습
            model.train()
            optimizer.zero_grad()

            # Forward pass
            outputs = model(features)
            loss = criterion(outputs, label)
            print("Loss before backpropagation:", loss.item())
            print("Weights and biases before training:")
            print(model.fc1.weight)
            print(model.fc1.bias)

            # Backward pass
            loss.backward()
            optimizer.step()
            print("Weights and biases after training:")
            print(model.fc1.weight)
            print(model.fc1.bias)
            print(f"Loss: {loss.item()}")
            logger.info(f"Training loss at epoch {epoch}: {loss.item()}")

            # 사용자별 학습 상태 저장
            model_manager.save_model(user_id, model, optimizer, epoch)

            # 학습 상태 저장
            save_training_state(user_id, epoch, model, optimizer)

        except Exception as e:
            logger.error(f"Error during training: {e}")
            raise
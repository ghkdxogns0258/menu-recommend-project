import os
import torch
from flask import Blueprint, jsonify, request
from db.user_db import get_user_profile
from model.recommendation_model import MenuRecommendationNet
from utils.data.data_loader import load_menu_data
from utils.training.file_manager import get_weights_path
from utils.logging.logger import logger
from utils.model_manager import ModelManager


recommend_blueprint = Blueprint('recommend', __name__)

# 메뉴 데이터 로드
menu_data = load_menu_data()
if not menu_data or "menu_features" not in menu_data[0]:
    raise ValueError("Invalid menu_data: 'menu_features' key is missing or data is empty.")

# 입력 크기와 메뉴 수
input_size = 11  # menu_features(5) + 시간(3) + 날씨(3)
num_menus = len(menu_data)

# 모델 생성
model = MenuRecommendationNet(input_size=input_size, num_menus=num_menus)

model_manager = ModelManager(input_size=11, num_menus=len(menu_data))

@recommend_blueprint.route('/recommend', methods=['GET'])
def recommend():
    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify({"error": "user_id is required"}), 400

    # 사용자별 파일 락을 사용해 동시성 관리
    with model_manager.get_lock(user_id):
        # 사용자별 모델 가져오기
        model = model_manager.get_model(user_id)
        # 사용자별 옵티마이저 가져오기 (학습된 옵티마이저)
        optimizer = model_manager.get_optimizer(user_id)

        # 사용자 선호도 및 입맛 정보
        user_profile = get_user_profile(user_id)
        preferences = [
            user_profile.preferences.get("taste", 0.5),
            user_profile.preferences.get("value", 0.5),
            user_profile.preferences.get("health", 0.5),
            user_profile.preferences.get("cooking", 0.5),
            user_profile.preferences.get("greasiness", 0.5),
            ]
        user_taste_profile = [
            user_profile.user_taste_profile.get("sweet", 0.5),
            user_profile.user_taste_profile.get("salty", 0.5),
            user_profile.user_taste_profile.get("spicy", 0.5),
            user_profile.user_taste_profile.get("sour", 0.5),
            user_profile.user_taste_profile.get("umami", 0.5),
        ]

    # 입력 데이터 준비
    inputs = []
    for menu in menu_data:
        menu_features_vector = list(menu["menu_features"].values())
        external_factors = [
            int(menu["time_morning"]),
            int(menu["time_lunch"]),
            int(menu["time_dinner"]),
            int(menu["weather_cold"]),
            int(menu["weather_hot"]),
            int(menu["weather_rainy"]),
        ]
        inputs.append(menu_features_vector + external_factors)

    # 입력 텐서를 PyTorch로 변환
    inputs_tensor = torch.tensor(inputs, dtype=torch.float32)
    print("Input features for recommendation:")
    print(inputs)
    # 모델 실행
    model.eval()
    with torch.no_grad():
        outputs = model(inputs_tensor).squeeze(-1)
    print("Model predictions:")
    print(outputs)


    # 추천 메뉴 선택
    recommended_index = torch.argmax(outputs).item()
    recommended_menu = menu_data[recommended_index]
    print("Recommended menu:")
    print(recommended_menu)
    return jsonify({
        "menu_name": recommended_menu["name"],
        "description": recommended_menu["description"],
        "cuisine_type": recommended_menu["cuisine_type"],
    })

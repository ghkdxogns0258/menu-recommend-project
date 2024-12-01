from flask import Blueprint, jsonify, request
from utils.model_manager import ModelManager
from db.user_db import get_user_profile

initialize_blueprint = Blueprint('initialize', __name__)
model_manager = ModelManager(input_size=11, num_menus=50)


@initialize_blueprint.route('/initialize-model', methods=['POST'])
def initialize_model():
    """
    사용자 정보를 기반으로 모델을 초기화하거나 저장된 상태를 유지합니다.
    """
    user_id = request.json.get('user_id')
    if not user_id:
        return jsonify({"error": "Missing user_id"}), 400

    # 사용자 프로필 조회
    user_profile = get_user_profile(user_id)
    if not user_profile:
        return jsonify({"error": "User profile not found"}), 404

    # 사용자 선호도 및 입맛 정보 확인
    preferences = user_profile.preferences or {
        "taste": 0.5,
        "value": 0.5,
        "health": 0.5,
        "cooking": 0.5,
        "greasiness": 0.5,
    }
    user_taste_profile = user_profile.user_taste_profile or {
        "sweet": 0.5,
        "salty": 0.5,
        "spicy": 0.5,
        "sour": 0.5,
        "umami": 0.5,
    }

    # 사용자 모델 초기화 (없을 경우에만 초기화)
    with model_manager.get_lock(user_id):
        model = model_manager.get_model(user_id)

        # 저장된 가중치가 없으면 초기화
        if not model_manager.has_saved_model(user_id):
            print("Initializing model weights with preferences and taste profile:")
            print("Preferences:", preferences)
            print("Taste Profile:", user_taste_profile)
            model.initialize_weights(
                preferences=[
                    preferences["taste"],
                    preferences["value"],
                    preferences["health"],
                    preferences["cooking"],
                    preferences["greasiness"],
                ],
                user_taste_profile=[
                    user_taste_profile["sweet"],
                    user_taste_profile["salty"],
                    user_taste_profile["spicy"],
                    user_taste_profile["sour"],
                    user_taste_profile["umami"],
                ],
            )
            print("Model initialized successfully. Weights and biases set.")
            model_manager.save_model(user_id, model, optimizer=None, epoch=0)
            return jsonify({"message": "Model initialized successfully"}), 200

    return jsonify({"message": "Model already initialized"}), 200

@initialize_blueprint.route('/reset-model', methods=['POST'])
def reset_model():
    """
    사용자의 모델을 초기 상태로 강제로 재설정합니다.
    """
    user_id = request.json.get('user_id')
    if not user_id:
        return jsonify({"error": "Missing user_id"}), 400

    # 사용자 프로필 조회
    user_profile = get_user_profile(user_id)
    if not user_profile:
        return jsonify({"error": "User profile not found"}), 404

    # 사용자 선호도 및 입맛 데이터 로드
    preferences = user_profile.preferences or {
        "taste": 0.5,
        "value": 0.5,
        "health": 0.5,
        "cooking": 0.5,
        "greasiness": 0.5,
    }
    user_taste_profile = user_profile.user_taste_profile or {
        "sweet": 0.5,
        "salty": 0.5,
        "spicy": 0.5,
        "sour": 0.5,
        "umami": 0.5,
    }

    # 모델 초기화 (강제로 초기화)
    with model_manager.get_lock(user_id):
        model = model_manager.get_model(user_id)

        # 초기 가중치와 편향 설정
        model.initialize_weights(
            preferences=[
                preferences["taste"],
                preferences["value"],
                preferences["health"],
                preferences["cooking"],
                preferences["greasiness"],
            ],
            user_taste_profile=[
                user_taste_profile["sweet"],
                user_taste_profile["salty"],
                user_taste_profile["spicy"],
                user_taste_profile["sour"],
                user_taste_profile["umami"],
            ],
        )

        # 초기화된 상태로 저장 (옵티마이저는 None으로 처리)
        model_manager.save_model(user_id, model, optimizer=None, epoch=0)

    return jsonify({"message": "Model reset to initial state"}), 200

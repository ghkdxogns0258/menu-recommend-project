from flask import Blueprint, jsonify, request
from utils.data.data_loader import load_menu_data
from utils.training.train import train_feedback
from utils.logging.logger import logger
from utils.training.normalization import normalize_features
from utils.model_manager import ModelManager  # 사용자별 모델 관리

feedback_blueprint = Blueprint('feedback', __name__)
menu_data = load_menu_data()  # 메뉴 데이터 로드
if not menu_data:
    raise ValueError("Menu data is empty.")

num_menus = len(menu_data)    # 동적으로 메뉴 개수 설정
model_manager = ModelManager(input_size=11, num_menus=num_menus)

@feedback_blueprint.route('/feedback', methods=['POST'])
def feedback():
    global epoch

    # 요청 데이터 로드
    data = request.json
    print(f"Received feedback data: {data}")  # 요청 데이터 로그 출력

    if not data:
        return jsonify({"error": "No data provided"}), 400
    user_id = data.get("user_id")
    menu_name = data.get("menu_name")
    liked = data.get("liked")

    if not menu_name or liked is None:  # 메뉴 이름이나 liked 필드가 없는 경우
        return jsonify({"error": "Invalid input"}), 400

    # 메뉴 데이터 로드
    menu_data = load_menu_data()
    menu = next((m for m in menu_data if m.get("name") == menu_name), None)
    if not menu:
        return jsonify({"error": "Menu not found"}), 404

    # `menu_features` 데이터 확인 및 정규화
    menu_features = menu.get("menu_features")
    if not isinstance(menu_features, dict):
        return jsonify({"error": "'menu_features' must be a dictionary"}), 400

    logger.debug(f"Original menu_features: {menu_features}")

    try:
        normalized_menu_features = normalize_features(menu_features)
        logger.debug(f"Normalized menu_features: {normalized_menu_features}")
    except ValueError as e:
        logger.error(f"Taste profile normalization failed: {e}")
        return jsonify({"error": f"Taste profile normalization failed: {e}"}), 400

    # 사용자별 epoch 값 가져오기
    try:
        user_epoch = model_manager.get_epoch(user_id)  # model_manager 인스턴스 사용
    except Exception as e:
        logger.error(f"Failed to retrieve epoch for user {user_id}: {e}")
        return jsonify({"error": "Failed to retrieve user epoch"}), 500

    # 학습 로직 호출
    train_feedback(menu, liked, user_id, user_epoch + 1)

    # epoch 업데이트
    epoch = user_epoch + 1

    return jsonify({"message": "Feedback processed"}), 200


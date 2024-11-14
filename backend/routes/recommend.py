import random
from flask import Blueprint, jsonify
from utils.data.data_loader import load_menu_data  # 메뉴 데이터 로드 함수 가져오기

recommend_blueprint = Blueprint('recommend', __name__)

@recommend_blueprint.route('/recommend', methods=['GET'])
def recommend():
    # 메뉴 데이터 로드
    menu_data = load_menu_data()
    
    # 랜덤 추천 예시
    if menu_data:
        recommended_item = random.choice(menu_data)
        return jsonify(recommended_item)
    else:
        return jsonify({"error": "No menu data available"}), 404
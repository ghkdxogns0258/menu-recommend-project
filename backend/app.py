# app.py

from flask import Flask, jsonify, request
from utils.training.train import train_feedback  # 학습 함수 가져오기
from utils.logging.logger import logger  # 로거 가져오기
from utils.data.data_loader import load_menu_data  # 데이터 로드 함수 가져오기
from utils.training.preprocess import normalize_features  # 정규화 함수 가져오기
import random

app = Flask(__name__)  # Flask 애플리케이션 생성
menu_data = load_menu_data()  # 메뉴 데이터 로드

# 랜덤 메뉴 추천 API
@app.route('/recommend', methods=['GET'])
def recommend_menu():
    menu = random.choice(menu_data)  # 랜덤으로 메뉴 선택
    logger.info(f"Recommended menu: {menu['name']}")  # 추천된 메뉴 로깅
    return jsonify(menu)  # JSON 형식으로 반환

# 피드백 수집 및 학습 API
@app.route('/feedback', methods=['POST'])
def feedback():
    data = request.json  # 클라이언트에서 JSON 데이터 수신
    menu_name = data.get("menu_name")  # 메뉴 이름 추출
    liked = data.get("liked")  # 좋아요 여부 추출

    # 메뉴 이름을 기반으로 메뉴 데이터 검색
    menu = next((m for m in menu_data if m["name"] == menu_name), None)
    if menu:
        normalized_features = normalize_features(menu['features'])  # 메뉴 특성 정규화
        menu['features'] = normalized_features  # 정규화된 특성 저장
        train_feedback(menu, liked)  # 피드백으로 학습 진행
        logger.info(f"Feedback processed for menu: {menu_name}, liked: {liked}")  # 로깅
        return jsonify({"message": "Feedback processed"}), 200  # 응답
    else:
        logger.warning(f"Menu not found: {menu_name}")  # 메뉴가 없을 경우 경고 로그
        return jsonify({"error": "Menu not found"}), 404  # 404 오류 반환

if __name__ == '__main__':
    app.run(port=5000)  # Flask 애플리케이션 실행
# app.py
import os
from dotenv import load_dotenv
from flask import Flask, jsonify, request, make_response
from flask_cors import CORS
from auth.oauth import oauth_blueprint
from routes.recommend import recommend_blueprint
from routes.feedback import feedback_blueprint
from utils.logging.clear_logs import clear_weight_logs
from db.database import initialize_db
import db.models  # 모델들을 미리 로드하여 순환 참조 문제 방지
from db.user_db import update_user_preferences, update_user_tastes, get_user_profile

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

# CORS 설정
CORS(
    app,
    supports_credentials=True,
    resources={r"/*": {"origins": ["http://localhost:3000"]}},
    methods=["GET", "POST", "OPTIONS"],
    allow_headers=["Content-Type", "Authorization"],
)

# 블루프린트 등록
app.register_blueprint(oauth_blueprint)
app.register_blueprint(recommend_blueprint)
app.register_blueprint(feedback_blueprint)

# 데이터베이스 초기화 - 여기서 테이블 생성
initialize_db()

# 서버 시작 시 로그 삭제
clear_weight_logs()

# 모든 경로에 대해 OPTIONS 메서드를 처리할 수 있도록 설정
@app.before_request
def handle_options_request():
    if request.method == "OPTIONS":
        response = make_response()
        response.headers["Access-Control-Allow-Origin"] = "http://localhost:3000"
        response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
        response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
        response.headers["Access-Control-Allow-Credentials"] = "true"
        return response
    
@app.route('/user/preferences', methods=['POST'])

def user_preferences():
    data = request.json  # JSON 데이터를 받아옴

    # 디버깅을 위한 로그 출력
    print("Received data:", data)  # 전체 데이터 구조 확인
    user_id = data.get("user_id")
    preferences = data.get("preferences")

    print("User ID:", user_id)  # user_id 확인
    print("Preferences:", preferences)  # preferences 데이터 구조 확인
    
    if not user_id or not preferences:
        return jsonify({"error": "Invalid data"}), 400
    
    # 데이터베이스 업데이트 (예: update_user_preferences 함수 호출)
    update_user_preferences(user_id, preferences)
    return jsonify({"message": "Preferences updated successfully"}), 200

# user_tastes 라우트 추가
@app.route('/user/tastes', methods=['POST'])
def user_tastes():
    data = request.json
    print("Received taste data:", data)  # 여기서 데이터 구조 확인
    user_id = data.get('user_id')
    tastes = data.get('tastes')
    print("User ID:", user_id)
    print("Tastes:", tastes)

    if user_id and tastes:
        # 사용자 프로필 확인
        user_profile = get_user_profile(user_id)
        
        if user_profile:
            # 기존 프로필에 입맛 정보 추가
            return update_user_tastes(user_id, tastes)
        else:
            return jsonify({"error": "User profile not found"}), 400
    else:
        return jsonify({"error": "Invalid data"}), 400

# 서버 시작
if __name__ == "__main__":
    app.run(debug=True)
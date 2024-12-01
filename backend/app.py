import os
from dotenv import load_dotenv
from flask import Flask, jsonify, request, make_response
from flask_cors import CORS
from routes.auth import auth_blueprint
from auth.oauth import oauth_blueprint
from routes.recommend import recommend_blueprint
from routes.feedback import feedback_blueprint
from routes.session import session_blueprint
from initialize.initialize_model import initialize_blueprint
from utils.logging.clear_logs import clear_weight_logs
from db.database import initialize_db
import db.models
from db.user_db import update_user_preferences, update_user_tastes, get_user_profile
import logging

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

# 로깅 설정
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

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
app.register_blueprint(auth_blueprint)
app.register_blueprint(recommend_blueprint)
app.register_blueprint(feedback_blueprint)
app.register_blueprint(session_blueprint)
app.register_blueprint(initialize_blueprint)

# 데이터베이스 초기화
initialize_db()

# 서버 시작 시 로그 삭제
clear_weight_logs()


# OPTIONS 요청 동적 처리
@app.before_request
def handle_options_request():
    if request.method == "OPTIONS":
        response = make_response()
        response.headers.update({
            "Access-Control-Allow-Origin": "http://localhost:3000",
            "Access-Control-Allow-Methods": "GET, POST, OPTIONS,feedback",
            "Access-Control-Allow-Headers": "Content-Type, Authorization",
            "Access-Control-Allow-Credentials": "true"
        })
        return response


# 사용자 선호도 업데이트
@app.route('/user/preferences', methods=['POST'])
def user_preferences():
    try:
        data = request.json
        logger.debug(f"Received preferences data: {data}")

        user_id = data.get("user_id")
        preferences = data.get("preferences")

        if not user_id or not preferences:
            return jsonify({"error": "Invalid data"}), 400

        # 데이터베이스 업데이트
        update_user_preferences(user_id, preferences)
        logger.info(f"Updated preferences for user_id {user_id}")
        return jsonify({"message": "Preferences updated successfully"}), 200

    except Exception as e:
        logger.error(f"Error updating preferences: {e}")
        return jsonify({"error": "Internal server error"}), 500


# 사용자 입맛 업데이트
@app.route('/user/tastes', methods=['POST'])
def user_tastes():
    try:
        # 요청 데이터 로깅
        data = request.json
        logger.debug(f"Received taste data: {data}")

        # 데이터 유효성 검사
        user_id = data.get("user_id")
        tastes = data.get("tastes")
        if not user_id or not tastes:
            return jsonify({"error": "Invalid data"}), 400

        # 사용자 프로필 확인
        try:
            user_profile = get_user_profile(user_id)
        except Exception as e:
            logger.error(f"Error fetching user profile: {e}")
            return jsonify({"error": "Failed to fetch user profile"}), 500

        if user_profile:
            try:
                # 사용자 입맛 업데이트
                response = update_user_tastes(user_id, tastes)
                if response:
                    logger.info(f"Updated tastes for user_id {user_id}")
                    return response
                else:
                    logger.warning("update_user_tastes returned None")
                    return jsonify({"error": "Failed to update user tastes"}), 500
            except Exception as e:
                logger.error(f"Error updating user tastes: {e}")
                return jsonify({"error": "Failed to update user tastes"}), 500
        else:
            return jsonify({"error": "User profile not found"}), 404

    except Exception as e:
        # 전역 예외 처리
        logger.error(f"Unexpected error: {e}")
        return jsonify({"error": "Internal server error"}), 500


# 서버 시작
if __name__ == "__main__":
    app.run(debug=True)
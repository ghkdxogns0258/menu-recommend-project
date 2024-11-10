# app.py
import os
from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from auth.oauth import oauth_blueprint, init_oauth
from routes.recommend import recommend_blueprint
from routes.feedback import feedback_blueprint
from utils.logging.clear_logs import clear_weight_logs

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")
CORS(app)

# 블루프린트 등록
app.register_blueprint(oauth_blueprint)
app.register_blueprint(recommend_blueprint)
app.register_blueprint(feedback_blueprint)

# OAuth 초기화
init_oauth(app)

# 서버 시작 시 로그 삭제
clear_weight_logs()

if __name__ == "__main__":
    app.run(debug=True)
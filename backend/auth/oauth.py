# auth/oauth.py
import os
import requests
from flask import Blueprint, redirect, url_for, session, jsonify, request
from dotenv import load_dotenv
from db.user_db import create_user, get_user_by_provider_id, get_user_profile, update_user_info_complete

# .env 파일 로드
dotenv_path = os.path.join(os.path.dirname(__file__), '../.env')
load_dotenv(dotenv_path)

oauth_blueprint = Blueprint('oauth', __name__)

# 로그인 라우트
@oauth_blueprint.route('/login/kakao')
def login_kakao():
    redirect_uri = url_for('oauth.authorize_kakao', _external=True)
    return redirect(f"https://kauth.kakao.com/oauth/authorize?client_id={os.getenv('KAKAO_CLIENT_ID')}&redirect_uri={redirect_uri}&response_type=code")

# Kakao 인증 후 리다이렉트 처리
@oauth_blueprint.route('/authorize/kakao')
def authorize_kakao():
    code = request.args.get('code')
    token_url = "https://kauth.kakao.com/oauth/token"
    token_data = {
        "grant_type": "authorization_code",
        "client_id": os.getenv("KAKAO_CLIENT_ID"),
        "client_secret": os.getenv("KAKAO_CLIENT_SECRET"),
        "redirect_uri": url_for('oauth.authorize_kakao', _external=True),
        "code": code,
    }

    # Kakao API로 토큰 요청
    token_response = requests.post(token_url, data=token_data)
    if token_response.status_code != 200:
        print(f"토큰 요청 실패: {token_response.json()}")
        return jsonify({"error": "OAuth token retrieval failed"}), 500

    # 액세스 토큰 가져오기
    token_json = token_response.json()
    access_token = token_json.get("access_token")

    # 사용자 정보 요청
    user_info_url = "https://kapi.kakao.com/v2/user/me"
    headers = {"Authorization": f"Bearer {access_token}"}
    user_info_response = requests.get(user_info_url, headers=headers)
    user_info = user_info_response.json()
    print("사용자 정보:", user_info)

    # 사용자 정보 처리
    provider_id = f"kakao_{user_info.get('id')}"
    provider = "kakao"

    # 사용자가 처음 로그인하는지 확인
    user = get_user_by_provider_id(provider_id)
    if not user:
        user_id = create_user(provider_id=provider_id, provider=provider)
        is_first_login = True
    else:
        user_id = user.id
        user_profile = get_user_profile(user_id)
        is_first_login = not user_profile.is_info_complete if user_profile else True

    # 세션에 사용자 정보 저장
    session['user_id'] = user_id
    session['is_first_login'] = is_first_login

   # 첫 로그인 여부에 따라 리다이렉트
    if is_first_login:
        return redirect(f'http://localhost:3000/user_info/intro?user_id={user_id}')
    else:
        return redirect(f'http://localhost:3000/main?user_id={user_id}')
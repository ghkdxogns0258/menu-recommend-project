import os
import requests
from flask import Blueprint, redirect, url_for, session, jsonify, request
from db.user_db import create_user, get_user_by_provider_id, get_user_profile

oauth_blueprint = Blueprint('oauth', __name__)

# 카카오 로그인 라우트
@oauth_blueprint.route('/login/kakao')
def login_kakao():
    """
    카카오 로그인 URL로 리다이렉트
    """
    redirect_uri = url_for('oauth.authorize_kakao', _external=True)
    kakao_auth_url = f"https://kauth.kakao.com/oauth/authorize?client_id={os.getenv('KAKAO_CLIENT_ID')}&redirect_uri={redirect_uri}&response_type=code"
    return redirect(kakao_auth_url)


@oauth_blueprint.route('/authorize/kakao')
def authorize_kakao():
    code = request.args.get('code')
    if not code:
        return jsonify({"error": "Authorization code not provided"}), 400

    # 카카오 API에서 액세스 토큰 요청
    token_url = "https://kauth.kakao.com/oauth/token"
    token_data = {
        "grant_type": "authorization_code",
        "client_id": os.getenv("KAKAO_CLIENT_ID"),
        "client_secret": os.getenv("KAKAO_CLIENT_SECRET"),
        "redirect_uri": url_for('oauth.authorize_kakao', _external=True),
        "code": code,
    }

    token_response = requests.post(token_url, data=token_data)

    if token_response.status_code != 200:
        print(f"Failed to fetch access token: {token_response.status_code}, {token_response.text}")
        return jsonify({"error": "Failed to retrieve access token"}), 500

    try:
        access_token = token_response.json().get("access_token")
    except ValueError as e:
        print(f"Failed to decode JSON: {e}")
        return jsonify({"error": "Invalid response from Kakao API"}), 500

    # 사용자 정보 요청
    user_info_url = "https://kapi.kakao.com/v2/user/me"
    headers = {"Authorization": f"Bearer {access_token}"}
    user_info_response = requests.get(user_info_url, headers=headers)

    if user_info_response.status_code != 200:
        print(f"Failed to fetch user info: {user_info_response.status_code}, {user_info_response.text}")
        return jsonify({"error": "Failed to retrieve user information"}), 500

    try:
        user_info = user_info_response.json()
    except ValueError as e:
        print(f"Failed to decode user info JSON: {e}")
        return jsonify({"error": "Invalid response from Kakao API"}), 500

    provider_id = f"kakao_{user_info.get('id')}"
    provider = "kakao"

    # 사용자 존재 여부 확인 및 생성
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
        return redirect(f"http://localhost:3000/user_info/intro?user_id={user_id}")
    else:
        return redirect(f"http://localhost:3000/main?user_id={user_id}")

# auth/oauth.py
import os
from authlib.integrations.flask_client import OAuth
from flask import Blueprint, redirect, url_for, session
from dotenv import load_dotenv
from db.user_db import create_user, get_user_by_username

load_dotenv()

oauth_blueprint = Blueprint('oauth', __name__)
oauth = OAuth()

# 카카오, 구글, 네이버 OAuth 설정
def init_oauth(app):
    oauth.init_app(app)
    oauth.register(
        name='kakao',
        client_id=os.getenv("KAKAO_CLIENT_ID"),
        client_secret=os.getenv("KAKAO_CLIENT_SECRET"),
        authorize_url='https://kauth.kakao.com/oauth/authorize',
        access_token_url='https://kauth.kakao.com/oauth/token',
        client_kwargs={'scope': 'profile_nickname,account_email'},
    )
    oauth.register(
        name='google',
        client_id=os.getenv("GOOGLE_CLIENT_ID"),
        client_secret=os.getenv("GOOGLE_CLIENT_SECRET"),
        authorize_url='https://accounts.google.com/o/oauth2/auth',
        access_token_url='https://oauth2.googleapis.com/token',
        client_kwargs={'scope': 'openid email profile'},
    )
    oauth.register(
        name='naver',
        client_id=os.getenv("NAVER_CLIENT_ID"),
        client_secret=os.getenv("NAVER_CLIENT_SECRET"),
        authorize_url='https://nid.naver.com/oauth2.0/authorize',
        access_token_url='https://nid.naver.com/oauth2.0/token',
        client_kwargs={'scope': 'profile'},
    )

# 로그인 라우트 정의
@oauth_blueprint.route('/login/<provider>')
def login(provider):
    redirect_uri = url_for(f'oauth.authorize_{provider}', _external=True)
    return oauth.create_client(provider).authorize_redirect(redirect_uri)

@oauth_blueprint.route('/authorize/kakao')
def authorize_kakao():
    return handle_oauth_login('kakao', 'https://kapi.kakao.com/v2/user/me')

@oauth_blueprint.route('/authorize/google')
def authorize_google():
    return handle_oauth_login('google', 'https://openidconnect.googleapis.com/v1/userinfo')

@oauth_blueprint.route('/authorize/naver')
def authorize_naver():
    return handle_oauth_login('naver', 'https://openapi.naver.com/v1/nid/me')

def handle_oauth_login(provider, user_info_url):
    token = oauth.create_client(provider).authorize_access_token()
    user_info = oauth.create_client(provider).get(user_info_url).json()
    username = f"{provider}_{user_info.get('id')}"
    email = user_info.get('email', None)
    if not get_user_by_username(username):
        create_user(username=username, password_hash=None, email=email)
    session['user'] = username
    return redirect('/')

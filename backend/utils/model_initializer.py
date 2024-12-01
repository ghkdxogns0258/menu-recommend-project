# utils/model_initializer.py
import requests

def initialize_user_model(user_id):
    """
    사용자 모델 초기화를 처리합니다.
    """
    initialize_url = "http://localhost:5000/initialize-model"
    response = requests.post(initialize_url, json={"user_id": user_id})

    if response.status_code != 200:
        print(f"Failed to initialize model for user {user_id}: {response.text}")
        raise Exception("Model initialization failed")

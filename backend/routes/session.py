from flask import Blueprint, jsonify
import requests
from db.user_db import get_user_by_provider_id

session_blueprint = Blueprint('session', __name__)

@session_blueprint.route('/sync-session', methods=['GET'])
def sync_session():
    """
    클라이언트가 전달한 provider_id를 통해 사용자 확인:
    - user_id를 반환
    """
    provider_id = requests.args.get('provider_id')  # 클라이언트에서 전달
    if not provider_id:
        return jsonify({"error": "provider_id is required"}), 400

    user = get_user_by_provider_id(provider_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    return jsonify({"user_id": user.id})

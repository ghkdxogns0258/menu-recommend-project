from flask import Blueprint, jsonify, session

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/auth/user-id', methods=['GET'])
def get_user_id():
    """
    세션에 저장된 사용자 ID를 반환합니다.
    """
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({"error": "User not logged in"}), 401

    return jsonify({"user_id": user_id}), 200

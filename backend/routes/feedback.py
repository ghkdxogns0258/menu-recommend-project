from flask import Blueprint, jsonify, request
from utils.training.train import train_feedback
from utils.logging.logger import logger
from utils.training.preprocess import normalize_features

feedback_blueprint = Blueprint('feedback', __name__)
epoch = 1

@feedback_blueprint.route('/feedback', methods=['POST'])
def feedback():
    global epoch
    data = request.json
    menu_name = data.get("menu_name")
    liked = data.get("liked")

    menu = next((m for m in menu_data if m["name"] == menu_name), None)
    if menu:
        normalized_features = normalize_features(menu['features'])
        menu['features'] = normalized_features
        train_feedback(menu, liked, epoch)
        logger.info(f"Feedback processed for menu: {menu_name}, liked: {liked}, epoch: {epoch}")
        epoch += 1
        return jsonify({"message": "Feedback processed"}), 200
    else:
        logger.warning(f"Menu not found: {menu_name}")
        return jsonify({"error": "Menu not found"}), 404

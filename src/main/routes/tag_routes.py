from flask import Blueprint, request, jsonify

tags_routes_bp = Blueprint('tags_routes', __name__)

@tags_routes_bp.route('/create_tag', methods=['POST'])
def crate_tags():
    print(request.json)
    return jsonify({"success": "ok"}), 200

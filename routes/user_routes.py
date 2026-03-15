from flask import Blueprint, request, jsonify
from services.user_service import UserService


users_bp = Blueprint("users", __name__)


@users_bp.get("/")
def get_all_users():
    return jsonify(UserService.get_all_users())

@users_bp.get("/<int:user_id>")
def get_user(user_id):
    user = UserService.get_user(user_id)
    return jsonify(user or {})

@users_bp.post("/")
def create_user():
    data = request.json
    return jsonify(UserService.create_user(data)), 201

@users_bp.put("/<int:user_id>")
def update_user(user_id):
    data = request.json
    return jsonify(UserService.update_user(user_id, data))

@users_bp.delete("/<int:user_id>")
def delete_user(user_id):
    return jsonify(UserService.delete_user(user_id))

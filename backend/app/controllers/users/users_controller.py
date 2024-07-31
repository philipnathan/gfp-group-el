from flask import request
from flask_login import login_required
from flask_jwt_extended import jwt_required, get_jwt_identity

from . import users_blueprint
from .users_services import UserServices

service = UserServices()


@users_blueprint.route("/login", methods=["POST"])
def user_login():
    data = request.get_json()
    return service.user_login(data)


@users_blueprint.route("register", methods=["POST"])
def user_register():
    data = request.get_json()
    return service.user_register(data)


@users_blueprint.route("/logout", methods=["POST"])
@login_required
def user_logout():
    return service.user_logout()


@users_blueprint.route("/me", methods=["GET"])
@jwt_required()
def user_info():
    identity = get_jwt_identity()
    user_id = identity.get("id")
    return service.user_info(user_id)


@users_blueprint.route("/update", methods=["PUT"])
@jwt_required()
def user_edit():
    identity = get_jwt_identity()
    user_id = identity.get("id")
    data = request.get_json()
    return service.user_edit(user_id, data)


@users_blueprint.route("/delete", methods=["DELETE"])
@jwt_required()
def user_delete():
    identity = get_jwt_identity()
    user_id = identity.get("id")
    data = request.get_json()
    return service.user_delete(user_id, data)

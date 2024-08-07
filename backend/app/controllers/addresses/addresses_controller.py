from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity

from .addresses_service import AddressesService
from . import addresses_blueprint

service = AddressesService()


@addresses_blueprint.route("/create", methods=["POST"])
@jwt_required()
def user_address_create():
    data = request.get_json()
    identity = get_jwt_identity()
    rt_rw = data.get("rt_rw")
    return service.create_address(data, identity, rt_rw)


@addresses_blueprint.route("/update/<int:address_id>", methods=["PUT"])
@jwt_required()
def address_update(address_id):
    data = request.get_json()
    identity = get_jwt_identity()
    return service.edit_adress(data, identity, address_id)


@addresses_blueprint.route("/delete/<int:address_id>", methods=["DELETE"])
@jwt_required()
def address_delete(address_id):
    identity = get_jwt_identity()
    return service.delete_address(identity, address_id)


@addresses_blueprint.route("/list", methods=["GET"])
@jwt_required()
def address_list():
    identity = get_jwt_identity()
    return service.list_address(identity)


@addresses_blueprint.route("/list/<int:address_id>", methods=["GET"])
@jwt_required()
def address_by_id(address_id):
    identity = get_jwt_identity()
    return service.get_address_by_id(identity, address_id)

from flask_jwt_extended import jwt_required

from . import shipments_blueprint
from .shipments_service import ShipmentsService

service = ShipmentsService()


@shipments_blueprint.route("/list", methods=["GET"])
@jwt_required()
def shipment_list():
    return service.list_shipments()

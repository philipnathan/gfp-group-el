from . import shipments_blueprint
from .shipments_service import ShipmentsService

service = ShipmentsService()


@shipments_blueprint.route("/list", methods=["GET"])
def shipment_list():
    return service.list_shipments()

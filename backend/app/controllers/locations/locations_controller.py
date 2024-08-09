from flask import request
from flasgger import swag_from

from . import locations_blueprint
from .locations_services import LocationServices


service = LocationServices()


@locations_blueprint.route("/provinces", methods=["GET"])
@swag_from("./location_all_provinces.yml")
def get_provinces():
    pass


#     return service.get_provinces()


# @locations_blueprint.route("/districts", methods=["GET"])
# @swag_from("./location_all_districts.yml")
# def get_districts():
#     return service.get_districts()


# @locations_blueprint.route("/subdistricts", methods=["GET"])
# @swag_from("./location_all_subdistricts.yml")
# def get_subdistricts():
#     return service.get_subdistricts()


# @locations_blueprint.route("/search", methods=["GET"])
# @swag_from("./location_by_id.yml")
# def get_location():
#     prov_id = request.args.get("prov_id", type=int)
#     dist_id = request.args.get("dist_id", type=int)
#     subdist_id = request.args.get("subdist_id", type=int)
#     return service.get_location_by_id(prov_id, dist_id, subdist_id)

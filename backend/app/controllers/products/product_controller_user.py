from flask import request

from . import products_blueprint
from .products_services import ProductsServices
from .product_services_user import ProductServicesUser

service = ProductsServices()
user_service = ProductServicesUser()


@products_blueprint.route("/user", methods=["GET"])
def get_products():
    req = request
    return service.get_list_products(req, "user")


@products_blueprint.route("/user/product/<int:product_id>", methods=["GET"])
def get_product_by_id(product_id):
    return service.get_product_by_id(product_id, "user")


@products_blueprint.route("/user/category/<int:category_id>", methods=["GET"])
def get_product_by_category(category_id):
    req = request
    return user_service.get_product_by_category(category_id, req)


@products_blueprint.route("/user/query", methods=["GET"])
def get_product_by_filter():
    req = request
    return user_service.get_product_by_filter(req)

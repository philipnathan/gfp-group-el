from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity

from . import reviews_blueprint
from .reviews_service import ReviewsService

service = ReviewsService()


## mungkin bisa diganti jadi transaction_id
@reviews_blueprint.route("/create/<int:product_id>", methods=["POST"])
@jwt_required()
def review_create(product_id):
    data = request.get_json()
    identity = get_jwt_identity()
    data["user_id"] = identity.get("id")
    data["role"] = identity.get("role")
    return service.create_review(data, product_id)

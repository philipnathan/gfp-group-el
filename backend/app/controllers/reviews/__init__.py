from flask import Blueprint

reviews_blueprint = Blueprint("reviews_blueprint", __name__, url_prefix="/api/reviews")

from . import reviews_contoller

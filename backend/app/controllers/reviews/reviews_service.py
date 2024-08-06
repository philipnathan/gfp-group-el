from .reviews_repository import ReviewsRepository
from app.db import db
from ..common import is_filled, get_data_and_validate
from ..products.products_repository import ProductsRepository


class ReviewsService:
    def __init__(self, db=db, repository=None, product_repository=None):
        self.db = db
        self.repository = repository or ReviewsRepository()
        self.product_repository = product_repository or ProductsRepository()

    def create_review(self, data, product_id):
        try:
            review = get_data_and_validate(
                data, review=str, rating=float, user_id=int, role=str
            )

            if not is_filled(**review):
                raise ValueError("Please fill all required fields")

            if review["role"] == "seller":
                raise ValueError("Seller cannot leave a review")

            # check apakah 'user id' melakukan transaksi dengan 'transaction id'

            product = self.product_repository.get_product_by_id(
                role=review["role"], product_id=product_id
            )

            if product is None:
                raise ValueError("Product not found")

            product = product.to_dict()
            review["product_id"] = product_id
            review["seller_id"] = product["seller_id"]

            review = self.repository.create_review(**review)

            self.db.session.add(review)
            self.db.session.commit()

            return {"message": "Review created successfully"}, 200
        except ValueError as e:
            self.db.session.rollback()
            return {"error": str(e)}, 400
        except Exception as e:
            self.db.session.rollback()
            return {"error": str(e)}, 500

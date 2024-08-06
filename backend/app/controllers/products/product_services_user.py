from app.db import db
from . import products_repository


class ProductServicesUser:
    def __init__(self, db=db, repository=None):
        self.db = db
        self.repository = repository or products_repository.ProductsRepository()

    def get_product_by_category(self, category_id, request):
        try:
            page = request.args.get("page", 1, int)
            per_page = request.args.get("per_page", 10, int)

            products = self.repository.get_product_by_category(
                category_id=category_id, page=page, per_page=per_page
            )

            if not products:
                raise ValueError("Product not found / Invalid Category ID")

            return [product.to_dict() for product in products], 200
        except ValueError as e:
            return {"error": str(e)}, 400
        except Exception as e:
            return {"error": str(e)}, 500

    def get_product_by_filter(self, req):
        rating = req.args.get("rating", None)
        price = req.args.get("price", None)
        date = req.args.get("date", None)

        try:
            per_page = req.args.get("per_page", 10, int)
            page = req.args.get("page", 1, int)

            if rating and (rating == "desc" or rating == "asc"):
                products = self.repository.get_product_sorted_by_rating(
                    rating=rating, per_page=per_page, page=page
                )

            if price and (price == "desc" or price == "asc"):
                products = self.repository.get_product_sorted_by_price(
                    price=price, per_page=per_page, page=page
                )

            if date and date == "newest":
                products = self.repository.get_product_sorted_by_date(
                    date=date, per_page=per_page, page=page
                )

            if not products:
                raise ValueError("Product not found / Invalid Filter")

            return [product.to_dict() for product in products], 200

        except ValueError as e:
            return {"error": str(e)}, 400
        except Exception as e:
            return {"error": str(e)}, 500

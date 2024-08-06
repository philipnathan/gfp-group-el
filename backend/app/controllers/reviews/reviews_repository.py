from app.db import db
from app.models import Reviews


class ReviewsRepository:
    def __init__(self, db=db, review=Reviews):
        self.db = db
        self.review = review

    def create_review(self, **data):
        return self.review(**data)

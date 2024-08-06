from app.db import db
from app.models import Addresses


class AddressesRepository:
    def __init__(self, db=db, address=Addresses):
        self.db = db
        self.address = address

    def create_address(self, data):
        return self.address(data)

    def get_list_address(self, role_id, role):
        if role == "user":
            return self.address.query.filter_by(user_id=role_id).all()

        if role == "seller":
            return self.address.query.filter_by(seller_id=role_id).all()

    def get_address_by_filter(self, address_id, role_id, role):
        if role == "user":
            return self.address.query.filter_by(user_id=role_id, id=address_id).first()

        if role == "seller":
            return self.address.query.filter_by(
                seller_id=role_id, id=address_id
            ).first()

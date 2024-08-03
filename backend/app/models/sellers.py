from sqlalchemy import (
    Column,
    Integer,
    VARCHAR,
    TEXT,
    SmallInteger,
    DateTime,
    ForeignKey,
)
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
import bcrypt
from enum import Enum

from ..db import db


class Is_Active_Status(Enum):
    INACTIVE = 0
    ACTIVE = 1


class Sellers(db.Model):
    __tablename__ = "sellers"

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(VARCHAR(50), unique=True, nullable=False)
    password = Column(VARCHAR(255), nullable=False)
    phone_number = Column(VARCHAR(14), unique=True, nullable=False)
    store_name = Column(VARCHAR(30), unique=True, nullable=False)
    store_description = Column(TEXT, nullable=True)
    store_address = Column(TEXT, nullable=True)
    store_subdistrict = Column(Integer, ForeignKey("subdistricts.id"), nullable=True)
    store_image_url = Column(VARCHAR(255), nullable=True)
    is_active = Column(
        SmallInteger, default=Is_Active_Status.ACTIVE.value, nullable=False
    )
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    shipping_options = relationship("ShippingOptions", backref="shipment_rel")
    seller_vouchers = relationship("SellerVouchers", backref="seller")
    transactions = relationship("Transactions", backref="seller")

    def __init__(self, email, password, phone_number, store_name):
        self.email = email
        self.password = self.set_password(password)
        self.phone_number = phone_number
        self.store_name = store_name

    def set_password(self, password):
        return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

    def check_password(self, password):
        return bcrypt.checkpw(password.encode("utf-8"), self.password.encode("utf-8"))

    def to_dict(self):
        return {
            "id": self.id,
            "email": self.email,
            "phone_number": self.phone_number,
            "store_name": self.store_name,
            "store_description": self.store_description,
            "store_address": self.store_address,
            "store_subdistrict": self.store_subdistrict,
            "store_image_url": self.store_image_url,
        }

    def delete_seller(self):
        self.is_active = Is_Active_Status.INACTIVE.value

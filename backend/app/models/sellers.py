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

from ..db import db


class Sellers(db.Model):
    __tablename__ = "sellers"

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(VARCHAR(50), unique=True, nullable=False)
    phone_number = Column(VARCHAR(14), unique=True, nullable=False)
    store_name = Column(VARCHAR(30), unique=True, nullable=False)
    store_description = Column(TEXT, nullable=True)
    store_address = Column(TEXT, nullable=False)
    store_sub_district = Column(
        SmallInteger, ForeignKey("locations.id"), nullable=False
    )
    store_image_url = Column(VARCHAR(255), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    shipping_options = relationship("ShippingOptions", backref="shipment_rel")
    seller_vouchers = relationship("SellerVouchers", backref="seller")
    transactions = relationship("Transactions", backref="seller")

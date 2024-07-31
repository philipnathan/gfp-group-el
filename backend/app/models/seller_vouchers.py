from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    VARCHAR,
    TEXT,
    SmallInteger,
    DateTime,
)
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from enum import Enum

from ..db import db


class Discount_Type(Enum):
    PERCENTAGE = 1
    FIXED_DISCOUNT = 2


class Is_Active_Status(Enum):
    INACTIVE = 0
    ACTIVE = 1


class SellerVouchers(db.Model):
    __tablename__ = "seller_vouchers"

    id = Column(Integer, primary_key=True, autoincrement=True)
    seller_id = Column(Integer, ForeignKey("sellers.id"), nullable=False)
    title = Column(VARCHAR(30), nullable=False)
    sub_title = Column(VARCHAR(100), nullable=False)
    description = Column(TEXT, nullable=False)
    discount_type = Column(Integer, nullable=False)
    percentage = Column(SmallInteger, default=0, nullable=False)
    min_purchase_amount = Column(Integer, nullable=False)
    max_discount_amount = Column(Integer, nullable=False)
    usage_limit = Column(SmallInteger, nullable=False)
    start_date = Column(DateTime(timezone=True), nullable=False)
    expiry_date = Column(DateTime(timezone=True), nullable=False)
    is_active = Column(Integer, default=Is_Active_Status.ACTIVE.value, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    seller_voucher_id = relationship("User_Seller_Vouchers", backref="seller_voucher")

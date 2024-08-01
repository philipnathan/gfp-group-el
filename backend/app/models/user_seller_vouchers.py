from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.sql import func

from ..db import db


class UserSellerVouchers(db.Model):
    __tablename__ = "user_seller_vouchers"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    seller_voucher_id = Column(
        Integer, ForeignKey("seller_vouchers.id"), nullable=False
    )
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

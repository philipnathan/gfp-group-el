from sqlalchemy import Column, Integer, DateTime, ForeignKey, event
from datetime import datetime
import pytz

from ..db import db


class UserSellerVouchers(db.Model):
    __tablename__ = "user_seller_vouchers"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    seller_voucher_id = Column(
        Integer, ForeignKey("seller_vouchers.id"), nullable=False
    )
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=True)


@event.listens_for(UserSellerVouchers, "before_insert")
def set_created_at(mapper, connection, target):
    target.created_at = datetime.now(pytz.UTC)


@event.listens_for(UserSellerVouchers, "before_update")
def set_updated_at(mapper, connection, target):
    target.updated_at = datetime.now(pytz.UTC)

from sqlalchemy import Column, Integer, DateTime, ForeignKey, event
from datetime import datetime
import pytz
from enum import Enum
from sqlalchemy.orm import relationship

from ..db import db


class Is_Used_Status(Enum):
    UNUSED = 0
    USED = 1


class UserSellerVouchers(db.Model):
    __tablename__ = "user_seller_vouchers"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    seller_voucher_id = Column(
        Integer, ForeignKey("seller_vouchers.id"), nullable=False
    )
    is_used = Column(Integer, default=Is_Used_Status.UNUSED.value, nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "seller_voucher_id": self.seller_voucher_id,
            "seller_voucher_detail": self.seller_voucher.to_dict(),
            "is_used": self.is_used,
        }

    def used_voucher(self):
        self.is_used = Is_Used_Status.USED.value


@event.listens_for(UserSellerVouchers, "before_insert")
def set_created_at(mapper, connection, target):
    target.created_at = datetime.now(pytz.UTC)


@event.listens_for(UserSellerVouchers, "before_update")
def set_updated_at(mapper, connection, target):
    target.updated_at = datetime.now(pytz.UTC)

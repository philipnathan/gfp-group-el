from sqlalchemy import Column, Integer, DateTime, SmallInteger, ForeignKey, VARCHAR
from sqlalchemy.sql import func
from enum import Enum

from ..db import db


class Payment_Status(Enum):
    SUCCESS = 1
    FAILED = 0


class PaymentDetails(db.Model):
    __tablename__ = "payment_details"

    id = Column(Integer, primary_key=True, autoincrement=True)
    # transaction_id = Column(Integer, nullable=False)
    payment_method = Column(
        SmallInteger, ForeignKey("payment_methods.id"), nullable=False
    )
    payment_date = Column(DateTime(timezone=True), nullable=False)
    amount = Column(Integer, nullable=False)
    payment_status = Column(Integer, nullable=True)
    image_url = Column(VARCHAR(255), nullable=True)
    reference_number = Column(VARCHAR(50), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

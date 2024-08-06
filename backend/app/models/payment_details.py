from sqlalchemy import (
    Column,
    Integer,
    DateTime,
    SmallInteger,
    ForeignKey,
    VARCHAR,
    event,
)
from enum import Enum
from datetime import datetime
import pytz

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
    created_at = Column(DateTime, nullable=False)


@event.listens_for(PaymentDetails, "before_insert")
def set_created_at(mapper, connection, target):
    target.created_at = datetime.now(pytz.UTC)

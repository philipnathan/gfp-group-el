from sqlalchemy import Column, VARCHAR, SmallInteger, Integer, DateTime, event
from datetime import datetime
import pytz


from ..db import db


class PaymentMethods(db.Model):
    __tablename__ = "payment_methods"

    id = Column(SmallInteger, primary_key=True, autoincrement=True)
    vendor_name = Column(VARCHAR(30), nullable=False)
    payment_type = Column(VARCHAR(30), nullable=False)
    min_transaction = Column(Integer, nullable=False)
    max_transaction = Column(Integer, nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=True)


@event.listens_for(PaymentMethods, "before_insert")
def set_created_at(mapper, connection, target):
    target.created_at = datetime.now(pytz.UTC)


@event.listens_for(PaymentMethods, "before_update")
def set_updated_at(mapper, connection, target):
    target.updated_at = datetime.now(pytz.UTC)

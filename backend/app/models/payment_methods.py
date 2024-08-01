from sqlalchemy import Column, VARCHAR, SmallInteger, Integer, DateTime
from sqlalchemy.sql import func


from ..db import db


class PaymentMethods(db.Model):
    __tablename__ = "payment_methods"

    id = Column(SmallInteger, primary_key=True, autoincrement=True)
    vendor_name = Column(VARCHAR(20), nullable=False)
    payment_type = Column(VARCHAR(30), nullable=False)
    min_transaction = Column(Integer, nullable=False)
    max_transaction = Column(Integer, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

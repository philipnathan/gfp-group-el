from sqlalchemy import Integer, Column, BOOLEAN, DateTime, ForeignKey, event
from sqlalchemy.orm import relationship
from datetime import datetime
import pytz

from ..db import db


class ShippingOptions(db.Model):
    __tablename__ = "shipping_options"

    id = Column(Integer, primary_key=True, autoincrement=True)
    shipment_id = Column(Integer, ForeignKey("shipments.id"), nullable=False)
    seller_id = Column(Integer, ForeignKey("sellers.id"), nullable=False)
    availibility = Column(BOOLEAN, default=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.now(pytz.UTC))
    updated_at = Column(DateTime, nullable=True, onupdate=datetime.now(pytz.UTC))

    transactions = relationship("Transactions", backref="shipping_options")

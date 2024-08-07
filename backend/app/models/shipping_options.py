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
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=True)

    transactions = relationship("Transactions", backref="shipping_options")


@event.listens_for(ShippingOptions, "before_insert")
def set_created_at(mapper, connection, target):
    target.created_at = datetime.now(pytz.UTC)


@event.listens_for(ShippingOptions, "before_update")
def set_updated_at(mapper, connection, target):
    target.updated_at = datetime.now(pytz.UTC)

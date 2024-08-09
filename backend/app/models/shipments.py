from sqlalchemy import (
    Column,
    SmallInteger,
    Integer,
    DateTime,
    ForeignKey,
    VARCHAR,
    event,
)
from sqlalchemy.orm import relationship
from datetime import datetime
import pytz

from ..db import db


class Shipments(db.Model):
    __tablename__ = "shipments"

    id = Column(Integer, primary_key=True, autoincrement=True)
    vendor_name = Column(VARCHAR(30), nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=True)

    shipping_options = relationship("ShippingOptions", backref="shipment")


@event.listens_for(Shipments, "before_insert")
def set_created_at(mapper, connection, target):
    target.created_at = datetime.now(pytz.UTC)


@event.listens_for(Shipments, "before_update")
def set_updated_at(mapper, connection, target):
    target.updated_at = datetime.now(pytz.UTC)

from sqlalchemy import Column, SmallInteger, Integer, DateTime, ForeignKey, VARCHAR
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from ..db import db


class Shipments(db.Model):
    __tablename__ = "shipments"

    id = Column(Integer, primary_key=True, autoincrement=True)
    vendor_name = Column(VARCHAR(30), nullable=False)
    arrival_subdistrict = Column(Integer, ForeignKey("subdistricts.id"), nullable=False)
    destination_subdistrict = Column(
        Integer, ForeignKey("subdistricts.id"), nullable=False
    )
    service_name = Column(VARCHAR(10), nullable=False)
    estimated_time = Column(SmallInteger, nullable=False)
    cost_per_kilo = Column(Integer, nullable=False)
    min_cost = Column(SmallInteger, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    shipping_options = relationship("ShippingOptions", backref="shipment")

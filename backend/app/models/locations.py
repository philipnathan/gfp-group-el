from sqlalchemy import Column, SmallInteger, VARCHAR, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from ..db import db


class Locations(db.Model):
    __tablename__ = "locations"

    id = Column(SmallInteger, primary_key=True)
    province = Column(VARCHAR(100), unique=False, nullable=False)
    district = Column(VARCHAR(100), unique=False, nullable=False)
    subdistrict = Column(VARCHAR(100), unique=False, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    arrival = relationship(
        "Shipments",
        foreign_keys="Shipments.arrival_sub_district",
        backref="arrival_sub_district_rel",
    )
    destination = relationship(
        "Shipments",
        foreign_keys="Shipments.destination_sub_district",
        backref="destination_sub_district_rel",
    )
    sellers = relationship("Sellers", backref="subdistrict")

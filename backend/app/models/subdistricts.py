from sqlalchemy import Column, SmallInteger, VARCHAR, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from ..db import db


class Subdistricts(db.Model):
    __tablename__ = "subdistricts"

    id = Column(SmallInteger, primary_key=True, autoincrement=True)
    subdistrict_name = Column(VARCHAR(30), unique=True, nullable=False)
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

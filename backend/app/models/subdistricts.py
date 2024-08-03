from sqlalchemy import Column, Integer, DateTime, VARCHAR, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from ..db import db


class Subdistricts(db.Model):
    __tablename__ = "subdistricts"

    id = Column(Integer, primary_key=True, autoincrement=True)
    district_id = Column(Integer, ForeignKey("districts.id"), nullable=False)
    subdistrict = Column(VARCHAR(100), unique=False, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    arrival = relationship(
        "Shipments",
        foreign_keys="Shipments.arrival_subdistrict",
        backref="arrival_sub_district_rel",
    )
    destination = relationship(
        "Shipments",
        foreign_keys="Shipments.destination_subdistrict",
        backref="destination_sub_district_rel",
    )
    sellers = relationship("Sellers", backref="subdistrict")

    def to_dict(self):
        return {
            "id": self.id,
            "district_id": self.district_id,
            "subdistrict": self.subdistrict,
        }

from sqlalchemy import Column, Integer, DateTime, VARCHAR, ForeignKey, event
from sqlalchemy.orm import relationship
from datetime import datetime
import pytz

from ..db import db


class Subdistricts(db.Model):
    __tablename__ = "subdistricts"

    id = Column(Integer, primary_key=True, autoincrement=True)
    district_id = Column(Integer, ForeignKey("districts.id"), nullable=False)
    subdistrict = Column(VARCHAR(100), unique=False, nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=True)

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
    addresses = relationship("Addresses", backref="subdistrict_addresses")

    def to_dict(self):
        return {
            "id": self.id,
            "district_id": self.district_id,
            "subdistrict": self.subdistrict,
        }


@event.listens_for(Subdistricts, "before_insert")
def set_created_at(mapper, connection, target):
    target.created_at = datetime.now(pytz.UTC)


@event.listens_for(Subdistricts, "before_update")
def set_updated_at(mapper, connection, target):
    target.updated_at = datetime.now(pytz.UTC)

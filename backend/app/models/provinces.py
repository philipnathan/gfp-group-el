from sqlalchemy import Column, SmallInteger, VARCHAR, DateTime, event
from sqlalchemy.orm import relationship
from datetime import datetime
import pytz

from ..db import db


class Provinces(db.Model):
    __tablename__ = "provinces"

    id = Column(SmallInteger, primary_key=True, autoincrement=False)
    province = Column(VARCHAR(100), unique=False, nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=True)

    district = relationship("Districts", backref="districts")
    addresses = relationship("Addresses", backref="province_addresses")

    def provinces_to_dict(self):
        return {"province": self.province}

    def to_dict(self):
        return {
            "id": self.id,
            "province": self.province,
        }


@event.listens_for(Provinces, "before_insert")
def set_created_at(mapper, connection, target):
    target.created_at = datetime.now(pytz.UTC)


@event.listens_for(Provinces, "before_update")
def set_updated_at(mapper, connection, target):
    target.updated_at = datetime.now(pytz.UTC)

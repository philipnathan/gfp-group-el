from sqlalchemy import (
    SmallInteger,
    Column,
    VARCHAR,
    DateTime,
    ForeignKey,
    Integer,
    event,
)
from sqlalchemy.orm import relationship
from datetime import datetime
import pytz

from ..db import db


class Districts(db.Model):
    __tablename__ = "districts"

    id = Column(Integer, primary_key=True, autoincrement=False)
    province_id = Column(SmallInteger, ForeignKey("provinces.id"), nullable=False)
    district = Column(VARCHAR(100), unique=False, nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=True)

    subdistrict = relationship("Subdistricts", backref="districts")
    addresses = relationship("Addresses", backref="district_addresses")

    def to_dict(self):
        return {
            "id": self.id,
            "province_id": self.province_id,
            "district": self.district,
        }


@event.listens_for(Districts, "before_insert")
def set_created_at(mapper, connection, target):
    target.created_at = datetime.now(pytz.UTC)


@event.listens_for(Districts, "before_update")
def set_updated_at(mapper, connection, target):
    target.updated_at = datetime.now(pytz.UTC)

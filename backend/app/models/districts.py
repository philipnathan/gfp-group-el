from sqlalchemy import SmallInteger, Column, VARCHAR, DateTime, ForeignKey, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from ..db import db


class Districts(db.Model):
    __tablename__ = "districts"

    id = Column(Integer, primary_key=True, autoincrement=False)
    province_id = Column(SmallInteger, ForeignKey("provinces.id"), nullable=False)
    district = Column(VARCHAR(100), unique=False, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    subdistrict = relationship("Subdistricts", backref="districts")
    addresses = relationship("Addresses", backref="district_addresses")

    def to_dict(self):
        return {
            "id": self.id,
            "province_id": self.province_id,
            "district": self.district,
        }

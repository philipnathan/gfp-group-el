from sqlalchemy import Column, SmallInteger, VARCHAR, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from ..db import db


class Provinces(db.Model):
    __tablename__ = "provinces"

    id = Column(SmallInteger, primary_key=True, autoincrement=False)
    province = Column(VARCHAR(100), unique=False, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    district = relationship("Districts", backref="districts")
    addresses = relationship("Addresses", backref="province_addresses")

    def provinces_to_dict(self):
        return {"province": self.province}

    def to_dict(self):
        return {
            "id": self.id,
            "province": self.province,
        }

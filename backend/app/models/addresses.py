from sqlalchemy import (
    Column,
    Integer,
    VARCHAR,
    TEXT,
    DateTime,
    ForeignKey,
    SmallInteger,
)
from sqlalchemy.sql import func
from enum import Enum

from ..db import db


class Is_Active_Status(Enum):
    INACTIVE = 0
    ACTIVE = 1


class Addresses(db.Model):
    __tablename__ = "addresses"

    id = Column(Integer, primary_key=True, autoincrement=True)
    receiver_name = Column(VARCHAR(30), nullable=False)
    phone_number = Column(VARCHAR(14), nullable=False)
    address_type = Column(VARCHAR(20), nullable=False)
    address_line = Column(TEXT, nullable=False)
    province_id = Column(SmallInteger, ForeignKey("provinces.id"), nullable=False)
    district_id = Column(Integer, ForeignKey("districts.id"), nullable=False)
    subdistrict_id = Column(Integer, ForeignKey("subdistricts.id"), nullable=False)
    rt_rw = Column(VARCHAR(5), nullable=True)
    postal_code = Column(VARCHAR(5), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    seller_id = Column(Integer, ForeignKey("sellers.id"), nullable=True)
    is_active = Column(
        SmallInteger, default=Is_Active_Status.ACTIVE.value, nullable=False
    )
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    def __init__(self, data):
        self.receiver_name = data["receiver_name"]
        self.phone_number = data["phone_number"]
        self.address_type = data["address_type"]
        self.address_line = data["address_line"]
        self.province_id = data["province_id"]
        self.district_id = data["district_id"]
        self.subdistrict_id = data["subdistrict_id"]
        self.postal_code = data["postal_code"]
        self.rt_rw = data["rt_rw"]
        self.user_id = data["user_id"]
        self.seller_id = data["seller_id"]

    def to_dict(self):
        return {
            "id": self.id,
            "receiver_name": self.receiver_name,
            "phone_number": self.phone_number,
            "address_type": self.address_type,
            "address_line": self.address_line,
            "province": self.province_addresses.province,
            "district": self.district_addresses.district,
            "subdistrict": self.subdistrict_addresses.subdistrict,
            "rt_rw": self.rt_rw,
            "postal_code": self.postal_code,
            "is_active": self.is_active,
        }

    def delete_address(self):
        self.is_active = Is_Active_Status.INACTIVE.value

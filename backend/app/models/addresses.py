from sqlalchemy import Column, Integer, VARCHAR, ForeignKey, TEXT, DateTime
from sqlalchemy.sql import func

from ..db import db


class Addresses(db.Model):
    __tablename__ = "addresses"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    receiver_name = Column(VARCHAR(30), nullable=False)
    phone_number = Column(VARCHAR(14), nullable=False)
    address_type = Column(VARCHAR(20), nullable=False)
    address_line = Column(TEXT, nullable=False)
    # province
    # city_district
    # sub_district
    # rt_rw
    postal_code = Column(VARCHAR(5), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

from sqlalchemy import Column, VARCHAR, SmallInteger, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from enum import Enum

from ..db import db


class Is_Active_Status(Enum):
    INACTIVE = 0
    ACTIVE = 1


class Categories(db.Model):
    __tablename__ = "categories"

    id = Column(SmallInteger, primary_key=True, autoincrement=True)
    category_name = Column(VARCHAR(30), unique=True, nullable=False)
    is_active = Column(
        SmallInteger, default=Is_Active_Status.ACTIVE.value, nullable=False
    )
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    products = relationship("Products", backref="category")

    def __init__(self, category_name):
        self.category_name = category_name

    def to_dict(self):
        return {"id": self.id, "category_name": self.category_name}

    def delete_category(self):
        self.is_active = Is_Active_Status.INACTIVE.value

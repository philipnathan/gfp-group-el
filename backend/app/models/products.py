from sqlalchemy.sql import func
from enum import Enum
from sqlalchemy import (
    Integer,
    VARCHAR,
    Text,
    Column,
    SmallInteger,
    ForeignKey,
    DateTime,
)

from app.db import db


class Product_Type(Enum):
    standard = 0
    premium = 1


class Products(db.Model):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(VARCHAR(255), nullable=False)
    description = Column(Text)
    price = Column(Integer, nullable=False)
    weight = Column(SmallInteger, nullable=False)
    volume = Column(SmallInteger, nullable=False)
    stock = Column(SmallInteger, nullable=False)
    image_url = Column(VARCHAR(255), nullable=True)
    product_type = Column(Integer, default=Product_Type.standard.value, nullable=False)
    category_id = Column(SmallInteger, ForeignKey("categories.id"), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    def __init__(
        self,
        name,
        description,
        price,
        weight,
        volume,
        stock,
        image_url,
        product_type,
        category_id,
    ):
        self.name = name
        self.description = description
        self.price = price
        self.weight = weight
        self.volume = volume
        self.stock = stock
        self.image_url = image_url
        self.product_type = product_type
        self.category_id = category_id

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "weight": self.weight,
            "volume": self.volume,
            "stock": self.stock,
            "image_url": self.image_url,
            "product_type": self.product_type.value,
            "category_id": self.category_id,
        }

    def upload_image(self):
        pass

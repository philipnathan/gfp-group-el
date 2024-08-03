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
    Float,
)

from app.db import db


class Product_Type(Enum):
    STANDARD = 0
    PREMIUM = 1


class Products(db.Model):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(VARCHAR(255), nullable=False)
    description = Column(Text, nullable=True)
    price = Column(Integer, nullable=False)
    weight_kg = Column(Float(5, 2), nullable=False)
    volume_m3 = Column(Float(5, 2), nullable=False)
    stock = Column(SmallInteger, nullable=False)
    image_url = Column(VARCHAR(255), nullable=True)
    product_type = Column(Integer, nullable=False)
    category_id = Column(SmallInteger, ForeignKey("categories.id"), nullable=False)
    seller_id = Column(Integer, ForeignKey("sellers.id"), nullable=False)
    is_active = Column(SmallInteger, default=1, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    def __init__(
        self,
        name,
        description,
        price,
        weight_kg,
        volume_m3,
        stock,
        image_url,
        product_type,
        category_id,
        seller_id,
    ):
        self.name = name
        self.description = description
        self.price = price
        self.weight_kg = weight_kg
        self.volume_m3 = volume_m3
        self.stock = stock
        self.image_url = image_url
        self.product_type = product_type
        self.category_id = category_id
        self.seller_id = seller_id

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "weight_kg": self.weight_kg,
            "volume_m3": self.volume_m3,
            "stock": self.stock,
            "image_url": self.image_url,
            "product_type": self.product_type,
            "category_id": self.category_id,
        }

    def upload_image(self):
        pass

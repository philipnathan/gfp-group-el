import bcrypt
from enum import Enum
from flask_login import UserMixin
from sqlalchemy import Column, Integer, VARCHAR, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from ..db import db


class Is_Active_Status(Enum):
    INACTIVE = 0
    ACTIVE = 1


class Users(db.Model, UserMixin):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(VARCHAR(30), unique=True, nullable=False)
    fullname = Column(VARCHAR(30), nullable=False)
    email = Column(VARCHAR(50), unique=True, nullable=False)
    password = Column(VARCHAR(255), nullable=False)
    phone_number = Column(VARCHAR(14), unique=True, nullable=False)
    is_active = Column(Integer, default=Is_Active_Status.ACTIVE.value, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    user_seller_vouchers = relationship("UserSellerVouchers", backref="user")
    transactions = relationship("Transactions", backref="user")
    addresses = relationship("Addresses", backref="user")

    def __init__(self, username, password, fullname, email, phone_number):
        self.username = username
        self.fullname = fullname
        self.email = email
        self.phone_number = phone_number
        self.password = self.set_password(password)

    def set_password(self, password):
        return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

    def check_password(self, password):
        return bcrypt.checkpw(password.encode("utf-8"), self.password.encode("utf-8"))

    def to_dict(self):
        return {
            "username": self.username,
            "fullname": self.fullname,
            "email": self.email,
            "phone_number": self.phone_number,
        }

    def delete_user(self):
        self.is_active = Is_Active_Status.INACTIVE.value

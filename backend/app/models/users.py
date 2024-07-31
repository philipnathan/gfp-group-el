import bcrypt
from flask_login import UserMixin
from sqlalchemy import Column, Integer, VARCHAR, DateTime
from sqlalchemy.sql import func

from ..db import db


class Users(db.Model, UserMixin):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(VARCHAR(30), unique=True, nullable=False)
    fullname = Column(VARCHAR(30), unique=True, nullable=False)
    email = Column(VARCHAR(50), unique=True, nullable=False)
    password = Column(VARCHAR(255), nullable=False)
    phone_number = Column(VARCHAR(14), unique=True, nullable=False)
    is_active = Column(Integer, default=1)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    def __init__(self, username, password, fullname, email, phone_number):
        self.username = username
        self.fullname = fullname
        self.email = email
        self.phone_number = phone_number
        self.password = self.set_password(password)

    def set_password(self, password):
        return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt("utf-8"))

    def check_password(self, password):
        return bcrypt.checkpw(password.encode("utf-8"), self.password.encode("utf-8"))

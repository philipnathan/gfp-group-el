from flask_login import login_user, logout_user, current_user
from flask_jwt_extended import create_access_token

from .users_repository import UserRepository
from app.db import db


class UserServices:
    def __init__(self, db=db, repository=None):
        self.repository = repository or UserRepository()
        self.db = db

    def user_login(self, data):
        email = data.get("email")
        password = data.get("password")

        try:
            user = self.repository.get_user_by_email(email)

            if user.is_active == 0:
                raise ValueError("Account is Inactive. Please contact customer service")

            if user is None or not user.check_password(password):
                raise ValueError("Invalid Email / Password")

            login_user(user)
            access_token = create_access_token(identity=user.id)

            return {"access_token": access_token}

        except ValueError as e:
            return {"error": str(e)}, 400
        except Exception as e:
            return {"error": str(e)}, 500

    def user_register(self, data):
        username = data.get("username")
        fullname = data.get("fullname")
        email = data.get("email")
        phone_number = data.get("phone_number")
        password = data.get("password")
        all_data = [username, fullname, email, phone_number, password]

        try:
            for data in all_data:
                if data is None:
                    raise ValueError("Please fill all required fields")

            is_email = self.repository.get_user_by_email(email)
            is_username = self.repository.get_user_by_username(username)
            is_phone_number = self.repository.get_user_by_phone_number(phone_number)

            if is_email.is_active == 0:
                raise ValueError("Please contact customer service")
            if is_email:
                raise ValueError("Email already exists")
            if is_username:
                raise ValueError("Username already exists")
            if is_phone_number:
                raise ValueError("Phone number already exists")

            user = self.repository.user_register(
                username=username,
                fullname=fullname,
                email=email,
                phone_number=phone_number,
                password=password,
            )

            self.db.session.add(user)
            self.db.session.commit()

            return {"message": "User created successfully"}, 201
        except ValueError as e:
            self.db.session.rollback()
            return {"error": str(e)}, 400
        except Exception as e:
            self.db.session.rollback()
            return {"error": str(e)}, 500

    def user_logout(self):
        logout_user()
        return {"message": "User logged out successfully"}, 200

    def user_info(self, user_id):
        try:
            if not current_user.is_authenticated:
                raise ValueError("Please login first")

            user = self.repository.get_user_by_id(user_id)

            return {"user": user.to_dict()}
        except ValueError as e:
            return {"error": str(e)}, 400
        except Exception as e:
            return {"error": str(e)}, 500

    def user_edit(self, user_id, data):
        request_type = data.get("request_type")

        if not current_user.is_authenticated:
            raise ValueError("Please login first")

        if request_type == "change_email":
            return self.change_email(user_id, data)

        if request_type == "change_password":
            return self.change_password(user_id, data)

    def user_delete(self, user_id, data):
        password = data.get("password")

        try:
            user = self.repository.get_user_by_id(user_id)

            if not user.check_password(password):
                raise ValueError("Incorrect password")

            user.delete_user()
            self.db.session.commit()

            return {"message": "User deleted successfully"}, 200

        except ValueError as e:
            self.db.session.rollback()
            return {"error": str(e)}, 400
        except Exception as e:
            self.db.session.rollback()
            return {"error": str(e)}, 500

    def change_email(self, user_id, data):
        new_email = data.get("new_email")
        password = data.get("password")

        if not new_email or not password:
            raise ValueError("Please fill all required fields")

        try:
            user = self.repository.get_user_by_id(user_id)

            if self.repository.get_user_by_email(new_email):
                raise ValueError("Email already exists")

            if not user.check_password(password):
                raise ValueError("Incorrect password")

            user.email = new_email
            self.db.session.commit()

            return {"message": "Email changed successfully"}, 200

        except ValueError as e:
            self.db.session.rollback()
            return {"error": str(e)}, 400
        except Exception as e:
            self.db.session.rollback()
            return {"error": str(e)}, 500

    def change_password(self, user_id, data):
        password = data.get("password")
        new_password = data.get("new_password")

        if not password or not new_password:
            raise ValueError("Please fill all required fields")

        try:
            user = self.repository.get_user_by_id(user_id)

            if not user.check_password(password):
                raise ValueError("Incorrect password")

            user.password = user.set_password(new_password)
            self.db.session.commit()

            return {"message": "Password changed successfully"}, 200

        except ValueError as e:
            self.db.session.rollback()
            return {"error": str(e)}, 400
        except Exception as e:
            self.db.session.rollback()
            return {"error": str(e)}, 500

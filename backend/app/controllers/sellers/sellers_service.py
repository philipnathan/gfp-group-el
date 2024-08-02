from flask_jwt_extended import create_access_token

from .sellers_repository import SellersRepository
from ..locations.locations_repository import LocationRepository
from app.db import db
from ..common import is_filled


class SellersServices:
    def __init__(self, db=db, repository=None, location=None):
        self.repository = repository or SellersRepository()
        self.location = location or LocationRepository()
        self.db = db

    def seller_login(self, data):
        email = data.get("email")
        password = data.get("password")

        try:
            if not is_filled(email, password):
                raise ValueError("Please fill all required fields")

            seller = self.repository.get_seller_by_email(email)

            if not seller:
                raise ValueError("Invalid email / password")

            if seller.is_active == 0:
                raise ValueError("Account is Inactive. Please contact customer service")

            if not seller.check_password(password):
                raise ValueError("Invalid email / password")

            access_token = create_access_token(
                identity={"id": seller.id, "role": "seller"}
            )

            return {"access_token": access_token}, 200

        except ValueError as e:
            return {"error": str(e)}, 400
        except Exception as e:
            return {"error": str(e)}, 500

    def seller_register(self, data):
        email = data.get("email")
        phone_number = data.get("phone_number")
        store_name = data.get("store_name")
        password = data.get("password")

        try:
            if not is_filled(email, phone_number, store_name, password):
                raise ValueError("Please fill all required fields")

            self.if_exist_raise_error(
                email=email, phone_number=phone_number, store_name=store_name
            )

            new_seller = self.repository.seller_register(
                email=email,
                phone_number=phone_number,
                store_name=store_name,
                password=password,
            )

            self.db.session.add(new_seller)
            self.db.session.commit()

            return {"message": "Seller registered successfully"}, 200

        except ValueError as e:
            self.db.session.rollback()
            return {"error": str(e)}, 400
        except Exception as e:
            self.db.session.rollback()
            return {"error": str(e)}, 500

    def seller_logout(self):
        try:
            return {"message": "Seller logged out successfully"}, 200
        except Exception as e:
            return {"error": str(e)}, 500

    def seller_info(self, seller_id):
        try:
            seller = self.repository.get_seller_by_id(seller_id)

            if not seller:
                raise ValueError("Seller not found")

            return {"seller": seller.to_dict()}
        except ValueError as e:
            return {"error": str(e)}, 400
        except Exception as e:
            return {"error": str(e)}, 500

    def seller_edit_personal(self, seller_id, data):
        request_type = data.get("request_type")

        if request_type == "change_email":
            return self.change_email(seller_id, data)

        if request_type == "change_password":
            return self.change_password(seller_id, data)

        if request_type == "change_phone_number":
            return self.change_phone_number(seller_id, data)

    def seller_edit_business(self, seller_id, data):
        all_data = {
            "store_name": data.get("store_name"),
            "store_description": data.get("store_description"),
            "store_address": data.get("store_address"),
            "store_subdistrict": data.get("store_subdistrict"),
            "store_image_url": data.get("store_image_url"),
        }

        try:
            seller = self.repository.get_seller_by_id(seller_id)
            count_updated_key = 0
            key_updated = []

            for key, data in all_data.items():
                # check if store_name is already used
                if key == "store_name" and data is not None:
                    self.if_exist_raise_error(store_name=data)

                # check if store_subdistrict is exist
                if key == "store_subdistrict" and data is not None:
                    if self.location.get_location_by_id(data) is None:
                        raise ValueError("Store subdistrict not found")

                # update if data is not None and seller has that key
                if data is not None and hasattr(seller, key):
                    setattr(seller, key, data)
                    count_updated_key += 1
                    key_updated.append(key)

            if count_updated_key == 0:
                raise ValueError("No data is updated")

            self.db.session.commit()

            return {
                "message": "Seller business information updated successfully",
                "key_updated": key_updated,
            }, 200

        except ValueError as e:
            self.db.session.rollback()
            return {"error": str(e)}, 400
        except Exception as e:
            self.db.session.rollback()
            return {"error": str(e)}, 500

    def seller_delete(self, seller_id, data):
        password = data.get("password")

        try:
            if not is_filled(password):
                raise ValueError("Please input your password")

            seller = self.repository.get_seller_by_id(seller_id)

            if not seller:
                raise ValueError("Seller not found")

            if seller.is_active == 0:
                raise ValueError("Seller already deleted")

            if not seller.check_password(password):
                raise ValueError("Incorrect password")

            seller.delete_seller()
            self.db.session.commit()

            return {"message": "Seller deleted successfully"}, 200

        except ValueError as e:
            self.db.session.rollback()
            return {"error": str(e)}, 400
        except Exception as e:
            self.db.session.rollback()
            return {"error": str(e)}, 500

    def change_email(self, seller_id, data):
        new_email = data.get("new_email")
        password = data.get("password")

        try:
            if not is_filled(new_email, password):
                raise ValueError("Please fill all required fields")

            seller = self.change_personal_checker(
                seller_id, password, "email", new_email
            )

            seller.email = new_email
            self.db.session.commit()

            return {"message": "Email changed successfully"}, 200

        except ValueError as e:
            self.db.session.rollback()
            return {"error": str(e)}, 400
        except Exception as e:
            self.db.session.rollback()
            return {"error": str(e)}, 500

    def change_password(self, seller_id, data):
        password = data.get("password")
        new_password = data.get("new_password")

        try:
            if not is_filled(password, new_password):
                raise ValueError("Please fill all required fields")

            seller = self.change_personal_checker(
                seller_id, password, "password", new_password
            )

            seller.password = seller.set_password(new_password)
            self.db.session.commit()

            return {"message": "Password changed successfully"}, 200

        except ValueError as e:
            self.db.session.rollback()
            return {"error": str(e)}, 400
        except Exception as e:
            self.db.session.rollback()
            return {"error": str(e)}, 500

    def change_phone_number(self, seller_id, data):
        password = data.get("password")
        new_phone_number = data.get("new_phone_number")

        try:
            if not is_filled(password, new_phone_number):
                raise ValueError("Please fill all required fields")

            seller = self.change_personal_checker(
                seller_id, password, "phone_number", new_phone_number
            )

            seller.phone_number = new_phone_number
            self.db.session.commit()

            return {"message": "Phone number changed successfully"}, 200

        except ValueError as e:
            self.db.session.rollback()
            return {"error": str(e)}, 400
        except Exception as e:
            self.db.session.rollback()
            return {"error": str(e)}, 500

    def change_personal_checker(self, seller_id, password, key, new_data):
        try:
            seller = self.repository.get_seller_by_id(seller_id)

            if not seller:
                raise ValueError("Seller not found")
            if not seller.check_password(password):
                raise ValueError("Incorrect password")
            if key != "password" and self.if_exist_raise_error(key, new_data):
                raise ValueError(f"{key} already used")

            return seller
        except ValueError as e:
            raise e
        except Exception as e:
            raise e

    def if_exist_raise_error(self, **kwargs):
        for key, value in kwargs.items():
            try:
                if key == "email" and self.repository.get_seller_by_email(value):
                    raise ValueError("Email already exists")
                if (
                    key == "phone_number"
                    and self.repository.get_seller_by_phone_number(value)
                ):
                    raise ValueError("Phone number already used")
                if key == "store_name" and self.repository.get_seller_by_store_name(
                    value
                ):
                    raise ValueError("Store name already used")
            except ValueError as e:
                raise e
            except Exception as e:
                raise e

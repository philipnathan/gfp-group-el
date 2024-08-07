from app.db import db
from .user_seller_vouchers_repository import UserSellerVouchersRepository
from ..users.users_repository import UserRepository
from ..seller_vouchers.seller_vouchers_repository import SellerVouchersRepository


class UserSellerVouchersService:
    def __init__(
        self,
        db=db,
        repository=None,
        user_repository=None,
        seller_voucher_repository=None,
    ):
        self.db = db
        self.repository = repository or UserSellerVouchersRepository()
        self.user_repository = user_repository or UserRepository()
        self.seller_voucher_repository = (
            seller_voucher_repository or SellerVouchersRepository()
        )

    def user_save_voucher(self, identity, voucher_id):
        try:
            user_id = identity.get("id")

            if self.user_repository.get_user_by_id(user_id) is None:
                raise ValueError("User not found")

            if identity.get("role") != "user":
                raise ValueError("Unauthorized")

            if self.repository.get_voucher_by_id_and_user_id(
                user_id=user_id, voucher_id=voucher_id
            ):
                raise ValueError("Voucher already saved")

            if (
                self.seller_voucher_repository.get_voucher_only_by_voucher_id(
                    voucher_id=voucher_id
                )
                is None
            ):
                raise ValueError("Voucher not found")

            voucher = self.repository.user_save_voucher(
                user_id=user_id, voucher_id=voucher_id
            )

            self.db.session.add(voucher)
            self.db.session.commit()

            return {"message": "Voucher saved successfully"}, 201
        except ValueError as e:
            self.db.session.rollback()
            return {"error": str(e)}, 400
        except Exception as e:
            self.db.session.rollback()
            return {"error": str(e)}, 500

    def user_list_vouchers(self, identity):
        try:
            if self.user_repository.get_user_by_id(identity.get("id")) is None:
                raise ValueError("User not found")

            if identity.get("role") != "user":
                raise ValueError("Unauthorized")

            user_id = identity.get("id")
            vouchers = self.repository.get_vouchers_by_user_id(user_id=user_id)

            if vouchers is None:
                raise ValueError("No vouchers found")

            return [voucher.to_dict() for voucher in vouchers], 200

        except ValueError as e:
            return {"error": str(e)}, 400
        except Exception as e:
            return {"error": str(e)}, 500

    def user_used_voucher(self, identity, user_seller_voucher_id):
        try:
            if self.user_repository.get_user_by_id(identity.get("id")) is None:
                raise ValueError("User not found")

            if identity.get("role") != "user":
                raise ValueError("Unauthorized")

            user_id = identity.get("id")
            voucher = self.repository.get_voucher_by_id_and_user_id(
                user_seller_voucher_id=user_seller_voucher_id, user_id=user_id
            )

            if voucher is None:
                raise ValueError("Voucher not found")
            if voucher.is_used == 1:
                raise ValueError("Voucher already used")

            voucher.used_voucher()
            self.db.session.commit()

            return {"message": "Voucher used successfully"}, 200
        except ValueError as e:
            self.db.session.rollback()
            return {"error": str(e)}, 400
        except Exception as e:
            self.db.session.rollback()
            return {"error": str(e)}, 500

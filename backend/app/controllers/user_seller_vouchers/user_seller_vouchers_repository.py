from datetime import datetime, timezone

from app.db import db
from app.models import UserSellerVouchers
from app.models import SellerVouchers


class UserSellerVouchersRepository:
    def __init__(self, db=db, voucher=UserSellerVouchers):
        self.db = db
        self.voucher = voucher

    def user_save_voucher(self, user_id, voucher_id):
        return self.voucher(user_id=user_id, seller_voucher_id=voucher_id)

    def get_vouchers_by_user_id(self, user_id):

        today = datetime.now(timezone.utc)
        query = (
            self.voucher.query.join(
                SellerVouchers, self.voucher.seller_voucher_id == SellerVouchers.id
            )
            .filter(self.voucher.user_id == user_id)
            .filter(SellerVouchers.expiry_date >= today)
            .all()
        )

        return query

    def get_voucher_by_id_and_user_id(self, user_id, user_seller_voucher_id):
        return self.voucher.query.filter_by(
            user_id=user_id, id=user_seller_voucher_id
        ).first()

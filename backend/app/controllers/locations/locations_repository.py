from app.db import db
from app.models import Provinces, Districts, Subdistricts


class LocationRepository:
    def __init__(
        self, db=db, province=Provinces, district=Districts, subdistrict=Subdistricts
    ):

        self.db = db
        self.province = province
        self.district = district
        self.subdistrict = subdistrict

    def get_provinces(self):
        return self.province.query.all()

    def get_districts(self):
        return self.district.query.all()

    def get_subdistricts(self):
        return self.subdistrict.query.all()

    def get_provinces_by_id(self, province_id):
        return self.province.query.filter_by(id=province_id).first()

    def get_districts_by_id(self, district_id):
        return self.district.query.filter_by(id=district_id).first()

    def get_subdistricts_by_id(self, subdistrict_id):
        return self.subdistrict.query.filter_by(id=subdistrict_id).first()

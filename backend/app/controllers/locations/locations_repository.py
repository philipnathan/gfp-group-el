from app.db import db
from app.models import Provinces, Districts, Subdistricts, Shipments

from sqlalchemy import or_


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
        query = (
            self.district.query.join(
                Subdistricts, Subdistricts.district_id == self.district.id
            )
            .join(
                Shipments,
                or_(
                    Shipments.arrival_subdistrict == self.subdistrict.id,
                    Shipments.destination_subdistrict == self.subdistrict.id,
                ),
            )
            .all()
        )

        return query

    def get_subdistricts(self):
        query = self.subdistrict.query.join(
            Shipments,
            or_(
                Shipments.arrival_subdistrict == self.subdistrict.id,
                Shipments.destination_subdistrict == self.subdistrict.id,
            ),
        ).all()

        return query

    def get_provinces_by_id(self, province_id):
        return self.province.query.filter_by(id=province_id).first()

    def get_districts_by_id(self, district_id):
        return self.district.query.filter_by(id=district_id).first()

    def get_subdistricts_by_id(self, subdistrict_id):
        return self.subdistrict.query.filter_by(id=subdistrict_id).first()

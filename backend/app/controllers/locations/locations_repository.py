from app.db import db
from app.models import Locations


class LocationRepository:
    def __init__(self, db=db, location=Locations):

        self.db = db
        self.location = location

    def get_location_by_id(self, id):
        return self.db.session.query(self.location).filter_by(id=id).first()

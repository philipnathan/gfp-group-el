import json
from app import create_app

from app.db import db
from app.models import Locations


def read_json(filename):
    with open(filename, "r") as f:
        return json.load(f)


def import_data(data):
    app = create_app()

    with app.app_context():
        try:
            for location in data:
                new_location = Locations(
                    id=location["id"],
                    province=location["province"],
                    district=location["district"],
                    subdistrict=location["subdistrict"],
                )
                db.session.add(new_location)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print(e)


import_data(read_json("location_data.json"))

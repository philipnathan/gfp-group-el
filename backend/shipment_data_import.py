import json
from app import create_app

from app.db import db

from app.models import Shipments


def read_json(filename):
    with open(filename) as f:
        return json.load(f)


def import_data(data, model):
    app = create_app()
    with app.app_context():
        try:
            for value in data:
                new_data = model(**value)

                db.session.add(new_data)
            db.session.commit()
            print("Data imported successfully")
        except Exception as e:
            db.session.rollback()
            print(e)


import_data(read_json("shipments.json"), Shipments)

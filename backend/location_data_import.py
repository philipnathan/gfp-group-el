import json
from app import create_app

from app.db import db
from app.models import Provinces, Districts, Subdistricts


def read_json(filename):
    with open(filename, "r") as f:
        return json.load(f)


def import_data(data, model):
    app = create_app()

    with app.app_context():
        try:
            for key, value in data.items():
                new_data = model(id=int(key), **value)
                db.session.add(new_data)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print(e)


import_data(read_json("province.json"), Provinces)
import_data(read_json("district.json"), Districts)
import_data(read_json("subdistrict.json"), Subdistricts)

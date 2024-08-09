from app.db import db
from .locations_repository import LocationRepository


class LocationServices:
    def __init__(self, db=db, repository=None):
        self.db = db
        self.repository = repository or LocationRepository()


#     def get_provinces(self):
#         try:
#             return [data.to_dict() for data in self.repository.get_provinces()]
#         except Exception as e:
#             return {"error": str(e)}, 500

#     def get_districts(self):
#         try:
#             return [data.to_dict() for data in self.repository.get_districts()]
#         except Exception as e:
#             return {"error": str(e)}, 500

#     def get_subdistricts(self):
#         try:
#             return [data.to_dict() for data in self.repository.get_subdistricts()]
#         except Exception as e:
#             return {"error": str(e)}, 500

#     def get_location_by_id(self, prov_id, dist_id, subdist_id):
#         try:
#             if subdist_id is not None:
#                 subdistrict = self.repository.get_subdistricts_by_id(subdist_id)
#                 if subdistrict is None:
#                     raise ValueError("Subdistrict not found")
#                 return subdistrict.to_dict()
#             if dist_id is not None:
#                 district = self.repository.get_districts_by_id(dist_id)
#                 if district is None:
#                     raise ValueError("District not found")
#                 return district.to_dict()
#             if prov_id is not None:
#                 province = self.repository.get_provinces_by_id(prov_id)
#                 if province is None:
#                     raise ValueError("Province not found")
#                 return province.to_dict()

#         except Exception as e:
#             return {"error": str(e)}, 500

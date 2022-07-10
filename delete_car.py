from flask_restful import Resource
from mock_cars_data import cars_in_system
from typing import Dict


class delete_car(Resource):
    # delete/deactivate a car in system
    def get(self, carId) -> Dict:
        for car in cars_in_system:
            if carId in cars_in_system:
                cars_in_system[car]["status"] = "deactivated from system"
                return {"Action": "deactivated",
                        "value": cars_in_system[car]}

            else:
                return {"Error": "car does not exist!"}
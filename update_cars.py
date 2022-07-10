from flask_restful import Resource
from mock_cars_data import cars_in_system
from typing import Dict


class update_cars(Resource):
    # update a car in system
    def get(self, carId: str, key: str, value: str) -> Dict:
        for car in cars_in_system:
            print(cars_in_system[car])
            if carId in cars_in_system.keys():
                cars_in_system[car][key] = value
                return cars_in_system[car]
            else:
                return {"Error": "car does not exist!"}

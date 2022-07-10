from flask_restful import Resource
from mock_cars_data import cars_in_system
from typing import Dict


class cars_list(Resource):
    # return the list of all cars in system
    def get(self) -> Dict:
        return cars_in_system

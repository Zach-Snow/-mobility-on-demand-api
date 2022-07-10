from flask_restful import Resource, reqparse, fields, marshal_with
from mock_cars_data import cars_in_system
from typing import Dict


class cars(Resource):
    # return the list of all cars in system
    def get(self) -> Dict:
        result = cars_in_system
        return result

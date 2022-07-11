from flask_restful import Resource, reqparse, fields, marshal_with
from mock_user_data import users_in_system
from typing import Dict


class users(Resource):
    # return the list of all cars in system
    def get(self) -> Dict:
        result = users_in_system
        return result

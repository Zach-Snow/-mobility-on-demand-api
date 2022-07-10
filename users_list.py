from flask_restful import Resource
from mock_user_data import users_in_system
from typing import Dict


class users_list(Resource):
    # return the list of all cars in system
    def get(self) -> Dict:
        return users_in_system

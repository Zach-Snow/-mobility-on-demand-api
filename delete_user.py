from flask_restful import Resource
from mock_user_data import users_in_system
from typing import Dict


class delete_user(Resource):
    # delete/deactivate an user in system
    def get(self, userId) -> Dict:
        for user in users_in_system:
            print(user)
            if userId in users_in_system.keys():
                if users_in_system[userId]["active_trip"]:
                    return {"Action": "Not performed as user in active trip",
                            "value": users_in_system[userId]}
                else:
                    users_in_system[userId]["status"] = "deactivated from system"
                    return {"Action": "deactivated",
                            "value": users_in_system[userId]}

            else:
                return {"Error": "user does not exist!"}
import json
from pprint import pprint

from flask_restful import Resource, reqparse, fields, marshal_with, abort
from mock_user_data import users_in_system
from typing import Dict

user_update_args = reqparse.RequestParser()
user_put_args = reqparse.RequestParser()

# All the arguments that can be updated
user_update_args.add_argument("name", type=str, default='')
user_update_args.add_argument("gender", type=str, default='')
user_update_args.add_argument("car_preference", type=list, default='')
user_update_args.add_argument("current_location", type=str, default='')
user_update_args.add_argument("destination_location", type=str, default='')
user_update_args.add_argument("current_location", type=str, default='')
user_update_args.add_argument("active_trip", type=bool, default='')
user_update_args.add_argument("active_vehicle", type=str, default='')
user_update_args.add_argument("status", type=str, default='')


# All the arguments are needed to input
user_put_args.add_argument("name", type=str, required=True)
user_put_args.add_argument("gender", type=str, required=True)
user_put_args.add_argument("age", type=str, required=True)
user_put_args.add_argument("car_preference", type=list, required=True)
user_put_args.add_argument("current_location", type=str, required=True)
user_put_args.add_argument("destination_location", type=str, required=True)
user_put_args.add_argument("active_trip", type=bool, required=True)
user_put_args.add_argument("active_vehicle", type=str, required=True)
user_put_args.add_argument("status", type=str, required=True)


#  TODO: Remember we only will need a resource fields dictionary when we want to use a database


class user_data(Resource):
    # return the list of detail for the id of the user inserted
    # TODO: remember, we need marshall_with only when we are using a db object for all the methods
    def get(self, userId: str = None) -> Dict:
        if not userId:
            return {"Message": "A valid user id is required!",
                    "Error": 404}
        else:
            try:
                result = users_in_system[userId]
            except KeyError:
                return {"Message": "The user id does not exist!",
                        "Error": 404}
            return result

    def put(self, userId: str = None) -> Dict:
        try:
            # This block checks to find if the id already exists in the database,
            # in my case the dictionary from mock data
            args = user_put_args.parse_args()
            # This is where the query into database happens
            result = users_in_system[userId]
            if result:
                return {"Message": "The user id already exists!",
                        "Error": 409}
        except KeyError:
            # This error only will happen when the id is an unique one
            # database code to entry the new data
            return_dictionary = {"Message": "Data has been entered",
                                 "Data": args}
            return return_dictionary

    # Method to update a key data for a user
    def patch(self, userId: str = None) -> Dict:
        # result = users_in_system[userId]
        # pprint(result)
        try:
            result = users_in_system[userId]
            args = user_update_args.parse_args()
            return_dict = {"Action": "Updated",
                           "arguments": args,
                           "after_action": ""}

            # TODO: Remember, this could be handled with a for loop,
            #  but for now as a prototype, its been handled like this
            if args['name']:
                result["name"] = args['name']
            if args['gender']:
                result["gender"] = args['gender']
            if args['car_preference']:
                result["car_preference"] = args['car_preference']
            if args['current_location']:
                result["current_location"] = args['current_location']
            if args['destination_location']:
                result["destination_location"] = args['destination_location']
            if args['active_trip']:
                result["active_trip"] = args['active_trip']
            if args['active_vehicle']:
                result["active_vehicle"] = args['active_vehicle']
            if args['status']:
                result["status"] = args['status']

            # TODO: Keep in mind when we use database, we have to commit the new update into database
            return_dict["after_action"] = result
            print(return_dict)
            return return_dict
        except KeyError:
            return {"Message": "A valid user id is required!",
                    "Error": 404}

    def delete(self, userId: str = None):
        try:
            result = users_in_system[userId]
            if users_in_system[userId]["active_trip"]:
                return {"Action": "Not performed as user in active trip",
                        "value": users_in_system[userId]}
            else:
                result["status"] = "deactivated from system"
                result["last_known_location"] = result["current_location"]
                del result["current_location"]

                return {"Action": "Deactivated, but reference kept in history.",
                        "after_action": result}

        except KeyError:
            return {"Error": "user does not exist!"}

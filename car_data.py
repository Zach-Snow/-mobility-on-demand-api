import json
from pprint import pprint

from flask_restful import Resource, reqparse, fields, marshal_with, abort
from mock_cars_data import cars_in_system
from typing import Dict

car_update_args = reqparse.RequestParser()
car_put_args = reqparse.RequestParser()

# All the arguments that can be updated
car_update_args.add_argument("model", type=str, default='')
car_update_args.add_argument("engine", type=str, default='')
car_update_args.add_argument("info_sys", type=str, default='')
car_update_args.add_argument("interior_design", type=str, default='')
car_update_args.add_argument("stopping_locations", type=list, default='')
car_update_args.add_argument("current_location", type=str, default='')
car_update_args.add_argument("next_location", type=str, default='')
car_update_args.add_argument("status", type=str, default='')


# All the arguments are needed to input
car_put_args.add_argument("model", type=str, required=True)
car_put_args.add_argument("engine", type=str, required=True)
car_put_args.add_argument("info_sys", type=str, required=True)
car_put_args.add_argument("interior_design", type=str, required=True)
car_put_args.add_argument("stopping_locations", type=list, required=True)
car_put_args.add_argument("current_location", type=str, required=True)
car_put_args.add_argument("next_location", type=str, required=True)
car_put_args.add_argument("status", type=str, required=True)


#  TODO: Remember we only will need a resource fields dictionary when we want to use a database


class cars_data(Resource):
    # return the list of detail for the id of the car inserted
    # TODO: remember, we need marshall_with only when we are using a db object for all the methods
    def get(self, carId: str = None) -> Dict:
        if not carId:
            return {"Message": "A valid car id is required!",
                    "Error": 404}
        else:
            try:
                result = cars_in_system[carId]
            except KeyError:
                return {"Message": "The car id does not exist!",
                        "Error": 404}
            return result

    def put(self, carId: str = None) -> Dict:
        try:
            # This block checks to find if the id already exists in the database,
            # in my case the dictionary from mock data
            args = car_put_args.parse_args()
            # This is where the query into database happens
            result = cars_in_system[carId]
            if result:
                return {"Message": "The car id already exists!",
                        "Error": 409}
        except KeyError:
            # This error only will happen when the id is an unique one
            # database code to entry the new data
            return_dictionary = {"Message": "Data has been entered",
                                 "Data": args}
            return return_dictionary

    # Method to update a key data for a car
    def patch(self, carId: str = None) -> Dict:
        try:
            args = car_update_args.parse_args()

            return_dict = {"Action": "Updated",
                           "arguments": args,
                           "after_action": ""}

            result = cars_in_system[carId]
            if args['model']:
                result["model"] = args['model']
            if args['engine']:
                result["engine"] = args['engine']
            if args['info_sys']:
                result["info_sys"] = args['info_sys']
            if args['interior_design']:
                result["interior_design"] = args['interior_design']
            if args['stopping_locations']:
                result["stopping_locations"] = args['stopping_locations']
            if args['current_location']:
                result["current_location"] = args['current_location']
            if args['next_location']:
                result["next_location"] = args['next_location']
            if args['status']:
                result["status"] = args['status']

            # TODO: Keep in mind when we use database, we have to commit the new update into database
            return_dict["after_action"] = result
            print(return_dict)
            return return_dict

        except KeyError:
            return {"Message": "A valid car id is required!",
                    "Error": 404}

    def delete(self, carId: str = None):
        try:
            result = cars_in_system[carId]
            result["status"] = "deactivated from system"
            result["last_known_location"] = result["current_location"]
            del result["current_location"]

            return {"Action": "Deactivated, but reference kept in history.",
                    "after_action": result}

        except KeyError:
            return {"Error": "car does not exist!"}

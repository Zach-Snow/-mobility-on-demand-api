import json
from pprint import pprint

from flask_restful import Resource, reqparse, fields, marshal_with, abort
from mock_cars_data import cars_in_system
from typing import Dict

car_update_args = reqparse.RequestParser()

# All the arguments that can be updated
car_update_args.add_argument("model", type=str, default='')
car_update_args.add_argument("engine", type=str, default='')
car_update_args.add_argument("info_sys", type=str, default='')
car_update_args.add_argument("interior_design", type=str, default='')
car_update_args.add_argument("stopping_locations", type=list, default='')
car_update_args.add_argument("current_location", type=str, default='')
car_update_args.add_argument("next_location", type=str, default='')
car_update_args.add_argument("status", type=str, default='')


#  TODO: Remember we only will need this when we want to use a database
# resource_fields = {
#     'carId': fields.String,
#     'model': fields.String,
#     'engine': fields.String,
#     'info_sys': fields.String,
#     'interior_design': fields.String,
#     'stopping_locations': fields.List,
#     'current_location': fields.String,
#     'next_location': fields.String,
#     'status': fields.String,
# }


class cars_data(Resource):
    # return the list of all cars in system
    # TODO: remember, we need marshall_with only when we are using a db object
    # @marshal_with(resource_fields)
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

    # @marshal_with(resource_fields)
    def patch(self, carId: str = None) -> Dict:
        try:
            args = car_update_args.parse_args()

            return_dict = {"Action": "Updated",
                           "arguments": list(args.keys()),
                           "after_action": ""}

            result = cars_in_system[carId]
            if args['model']:
                print("yes")
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

            return_dict["after_action"] = result
            print(return_dict)
            return return_dict

        except KeyError:
            return {"Message": "A valid car id is required!",
                    "Error": 404}

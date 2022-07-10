import os
import json
from flask import Flask
from flask_restful import Api
from root import Root
from cars import cars_list
from update_cars import update_cars
from delete_car import delete_car
from users_list import users_list
from delete_user import delete_user

app = Flask(__name__)
api = Api(app)

# Root path
api.add_resource(Root, "/")
# Route to list all cars
api.add_resource(cars_list, "/allCars")
# Route to update car detail using car id
api.add_resource(update_cars, "/update/<carId>/<key>/<value>")
# Route to delete car detail using car id
api.add_resource(delete_car, "/deleteCar/<carId>")
# Route to list all users
api.add_resource(users_list, "/allUsers")
# Route to delete/deactivate user detail using user id
api.add_resource(delete_user, "/deleteUser/<userId>")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)

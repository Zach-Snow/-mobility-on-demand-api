from flask import Flask
from flask_restful import Api
from root import Root
from cars import cars
from car_data import cars_data
from users import users
from user_data import user_data

app = Flask(__name__)
api = Api(app)

# Root path
api.add_resource(Root, "/")
# Route to list all cars
api.add_resource(cars, "/allcars")
# Route to update/delete/add car detail using car id or get data for specific car
api.add_resource(cars_data, "/car/<carId>",
                            "/car")
# Route to list all users
api.add_resource(users, "/allusers")
# Route to update/delete/add user detail using user id or get data for specific car
api.add_resource(user_data, "/user/<userId>",
                            "/user")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)

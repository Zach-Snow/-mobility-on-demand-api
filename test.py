from pprint import pprint

import requests

# TODO: Remember, this base path has to be changed based on which local ip the app uses at that time
base = "http://172.27.21.180:5001/"

# test for getting all the cars details
# response = requests.get(base+"allcars")

# test for getting a specific car details
# response = requests.get(base+"car/car_id_1")

# test for updating value in car
# response = requests.patch(base+"car/car_id_1", {"model": "value"})

# test for deletion
# response = requests.delete(base+"car/car_id_2")


# test to put car details
# new_car_details = {
#         "model": "Audi Q3 1.4",
#         "engine": "engine model for Audi Q3 1.4",
#         "info_sys": "infotainment system for Audi Q3 1.4",
#         "interior_design": "4 seater SUV",
#         "stopping_locations": ["stop_id_1", "stop_id_2", "stop_id_3"],
#         "current_location": "stop_id_1",
#         "next_location": "stop_id_2",
#         "status": "active"
#     }

# TODO: Remember you have to provide an unique car id when putting new value
# response = requests.put(base+"car/car_id_4", new_car_details)

# test for getting all the user details
# response = requests.get(base+"allusers")

# test for getting a specific user details
# response = requests.get(base+"user/user_id_1")

# test for updating value in existing user
# response = requests.patch(base+"user/user_id_1", {"name": "reese"})

# test for user deletion
# response = requests.delete(base+"user/user_id_2")

# test to put user details
new_user_details = {
    "name": "Doe John",
    "gender": "Male",
    "age": 28,
    # TODO: Remember this will be a bit error prone as we are not using a db at this moment,
    #  But as we will use db engine, this list will be as shown here.
    "car_preference": [{
        "model": "Audi Q3 1.4",
        "info_sys": "infotainment system for Audi Q3 1.4",
        "interior_design": "4 seater SUV",
    }],
    "current_location": "stop_id_1",
    "destination_location": "stop_id_3",
    "active_trip": False,
    "active_vehicle": "",
    "status": "active"
}

# TODO: Remember you have to provide an unique user id when putting new value
response = requests.put(base + "user/user_id_3", new_user_details)

pprint(response.json())

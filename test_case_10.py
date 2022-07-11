from pprint import pprint
import requests

# TODO: Remember, this base path has to be changed based on which local ip the app uses at that time,
#  so using localhost is the best option
base = "http://localhost:5001/"

# TODO: Remember, This will pass if the endpoint is working,
#  else, we will get an json decode error
# test for getting a specific car details

# TODO: the car id has to be a valid one from the database,
#  for example: ID: "user_id_4" will store the value in db (as its an unique id) ,
#               ID: "user_id_1" will show error and error code (as its not an unique id),
#           if json decode error happens, endpoint not working
user_id = "user_id_4"
# TODO: input any data you want to put in the dictionary for the new car id and run the script,
#  if json decode error happens, endpoint not working
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
# test for updating value in car
response = requests.put(base + f"user/{user_id}", new_user_details)

pprint(response.json())

from pprint import pprint

import requests

# TODO: Remember, this base path has to be changed based on which local ip the app uses at that time,
#  so using localhost is the best option
base = "http://localhost:5001/"

# TODO: Remember, This will pass if the endpoint is working,
#  else, we will get an json decode error
# test for getting a specific car details

# TODO: the car id has to be a valid one from the database,
#  for example: ID: "car_id_1" will show the value in db,
#               ID: "car_id_5" will show error and error code,
#           if json decode error happens, endpoint not working
car_id = "car_id_1"
# TODO: input any data you want to update in the dictionary and run the script,
#  if json decode error happens, endpoint not working

update_dictionary = {
        "model": "",
        "engine": "",
        "info_sys": "",
        "interior_design": "",
        "stopping_locations": "",
        "current_location": "",
        "next_location": "",
        "status": ""

}
# test for updating value in car
response = requests.patch(base+f"car/{car_id}", update_dictionary)


pprint(response.json())
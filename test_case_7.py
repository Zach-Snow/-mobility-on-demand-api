from pprint import pprint

import requests

# TODO: Remember, this base path has to be changed based on which local ip the app uses at that time,
#  so using localhost is the best option
base = "http://localhost:5001/"

# TODO: Remember, This will pass if the endpoint is working,
#  else, we will get an json decode error
# test for getting a specific car details

# TODO: Change the id here to see the effects, for
#  example: ID: "user_id_1" will show the value in db,
#           ID: "user_id_3" will show error and error code,
#           if json decode error happens, endpoint not working
user_id = "user_id_3"
response = requests.get(base+f"user/{user_id}")

pprint(response.json())
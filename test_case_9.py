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
#           ID: "user_id_5" will show error and error code,
#           if json decode error happens, endpoint not working, \
#           the data won't be deleted, rather kept in the database for historical purposes,
#           but it would have an identifier to determine if the id is in use or not, \
#           the id would not be deleted if the user is in an active trip (user_id_2)
user_id = "user_id_2"
response = requests.delete(base+f"user/{user_id}")

pprint(response.json())
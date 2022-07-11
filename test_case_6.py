from pprint import pprint

import requests

# TODO: Remember, this base path has to be changed based on which local ip the app uses at that time,
#  so using localhost is the best option
base = "http://localhost:5001/"

# test for getting all the cars details
# TODO: Remember, This will pass if the endpoint is working,
#  else, we will get an json decode error
response = requests.get(base+"allusers")

pprint(response.json())
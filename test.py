from pprint import pprint

import requests

base = "http://172.27.27.201:5001/"


# test for getting all the cars details\
response = requests.get(base+"allcars")

# # test for updating value in car
# response = requests.patch(base+"car/car_id_1", {"model": "value"})
pprint(response.json())
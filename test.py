from pprint import pprint

import requests

base = "http://172.27.27.201:5001/"


# test for getting all the cars details\
# response = requests.get(base+"allcars")

# test for updating value in car
# response = requests.patch(base+"car/car_id_1", {"model": "value"})

#test for deletion
# response = requests.delete(base+"car/car_id_2")
pprint(response.json())
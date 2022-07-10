from pprint import pprint

import requests

base = "http://172.27.27.201:5001/"


# test for getting all the cars details\
# response = requests.get(base+"allcars")

# test for updating value in car
# response = requests.patch(base+"car/car_id_1", {"model": "value"})

#test for deletion
# response = requests.delete(base+"car/car_id_2")


#test to put
dict_ = {
        "model": "Audi Q3 1.4",
        "engine": "engine model for Audi Q3 1.4",
        "info_sys": "infotainment system for Audi Q3 1.4",
        "interior_design": "4 seater SUV",
        "stopping_locations": ["stop_id_1", "stop_id_2", "stop_id_3"],
        "current_location": "stop_id_1",
        "next_location": "stop_id_2",
        "status": "active"
    }

response = requests.put(base+"car/car_id_3", dict_)
pprint(response.json())
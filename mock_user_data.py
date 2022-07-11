# mock data for users in system
users_in_system = {
    "user_id_1": {
        "name": "John Doe",
        "gender": "Male",
        "age": 24,
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
    },
    "user_id_2": {
        "name": "Jane Doe",
        "gender": "Female",
        "age": 24,
        "car_preference": [{
            "model": "Audi Q3 1.4",
            "info_sys": "infotainment system for Audi Q3 1.4",
            "interior_design": "4 seater SUV",
        }],
        "current_location": "stop_id_1",
        "destination_location": "stop_id_3",
        "active_trip": True,
        "active_vehicle": "car_id_1",
        "status": "active"
    },
}

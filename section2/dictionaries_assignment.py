my_vehicle = {
    "model": "Ford",
    "make": "Explorer",
    "year": 2018,
    "mileage": 40000
}

for keys, itens in my_vehicle.items():
    print(keys, itens)

vehicle2 = my_vehicle.copy()
vehicle2['number_of_tires'] = 4
vehicle2.pop('mileage')

for keys in vehicle2.keys():
    print(keys)
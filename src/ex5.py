from pprint import pprint

def build_car_list():
    ret_car_list = []
    car_dict = {}
    with open("./files/input.txt", "r") as file:
        next(file)
        for line in file:
            line = line.strip().split(",")
            id = int(line[0].strip())
            miles = line[1].strip()
            if miles.isdigit():
                miles = int(line[1].strip())
                car_dict[id] = miles

    car_model ={}
    with open("./files/car-ids.txt", "r") as car_id_file:
        for line in car_id_file:
            line = line.strip().split(",")
            id = int(line[0].strip())
            model = line[1].strip()
            car_model[id] = model
        print(car_model)
    
    for car_id, miles in car_dict.items():
        #print(car_model[1])
        ret_car_list.append({'id': car_id, 'miles': miles, 'model': car_model[car_id]})

    return ret_car_list

def ex5():
    car_list = build_car_list()
    pprint(car_list)

ex5()

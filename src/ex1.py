from ValidationException import ValidationException


def validate_file(input_file):
    with open(f"./files/{input_file}", "r") as file:
        next(file)
        for row in file:
            line = row.strip().split(",")
            car_id, mileage = line

            if not mileage.strip().isdigit():
                raise ValidationException(f"Invalid mileage: {mileage}")



def ex1():
    try:
        validate_file("input.txt")
    except ValidationException as ve:
        print(ve)

ex1()
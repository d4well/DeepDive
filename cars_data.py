from collections import namedtuple

def data_type_conv(data_type, value):
    if data_type == 'DOUBLE':
        return float(value)
    elif data_type == 'INT':
        return int(value)
    else:
        return str(value)

def cast_row(data_types, row):
    return [data_type_conv(data, value) for data, value in zip(data_types, row.strip().split(';'))]

with open('cars.csv') as f:
    f_iter = iter(f)
    headers_input = next(f_iter).strip().split(';')
    car = namedtuple('Car',headers_input)
    data_type = next(f_iter).strip().split(';')
    # cars = [car(*[data_type_conv(data, value) for data, value in zip(data_type,i.strip().split(';'))]) for i in f_iter]
    cars_data = [cast_row(data_type, row) for row in f_iter]
    cars = [car(*car_data) for car_data in cars_data]
    print(cars[2])



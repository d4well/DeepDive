# ##### Goal 1
# Create a lazy iterator that will return a named tuple of the data in each row. The data types should be appropriate
# - i.e. if the column is a date, you should be storing dates in the named tuple, if the field is an integer,
#  then it should be stored as an integer, etc.

##### Goal 2

# Calculate the number of violations by car make.

from collections import namedtuple
import datetime
from typing import Union

file_name = 'nyc_parking_tickets_extract.csv'

def type_correction(data_type: str, value: str) -> Union[int, str, datetime.datetime]:
    if data_type == 'INT':
        return int(value)
    elif data_type == 'DATE':
        # n_value = value.split('/')
        m, d, y = [int(i) for i in value.split('/')]
        return datetime.datetime(y,m,d)
    else:
        return str(value)

def cast_row(row):
    data_types = ['INT', 'STR', 'STR', 'STR','DATE','INT','STR','STR','STR']
    return [type_correction(data_type, value) for data_type, value in zip(data_types, row.strip().split(','))]

def violations_by_make(cars):
    violations = {}
    for car in cars:
        if car.VehicleMake in violations:
            violations[car.VehicleMake] += 1
        else:
            violations[car.VehicleMake] = 1
    return violations
    
def parse_file(file_name):
    with open(file_name) as f:
        headers = next(f).strip().split(',')
        headers_w = map(lambda i: i.replace(' ',''), headers)
        Car_headers = namedtuple('Car', headers_w)
        cars = (Car_headers(*cast_row(row)) for row in f)
        violations = violations_by_make(cars)
        sorted_violations = {k: v for k,v in sorted(violations.items(), key=lambda i: i[1], reverse=True)}
    return sorted_violations





# cars = [Car_headers(*cast_row(row)) for row in f]
 # print(sorted_violations)
# print(parse_file(file_name))
print(parse_file(file_name))
# date_format = '%m/%d/%Y'
# datetime.strptime(value,date_format).date()

import csv
from itertools import islice, chain, groupby, compress
from collections import namedtuple
from datetime import datetime

personal_info_data_types = ['STR', 'STR', 'STR', 'STR', 'STR']
employment_data_types = ['STR', 'STR', 'STR', 'STR']
update_status_data_types = ['STR', 'DATE', 'DATE']
vehicles_data_types = ['STR', 'STR', 'STR', 'INT']

personal_info_bool = [True, True, True, True, True]
employment_bool = [True, True, True, False]
update_status_bool = [False, True, True]
vehicles_bool = [False, True, True, True]

data_bools = tuple(chain(personal_info_bool, employment_bool, update_status_bool,
            vehicles_bool))

data_types_file = {
    'personal_info.csv': personal_info_data_types,
    'employment.csv': employment_data_types,
    'update_status.csv': update_status_data_types,
    'vehicles.csv': vehicles_data_types,
}

def read_data(file_name):
    with open(file_name) as f:
        rows = csv.reader(f, delimiter=',', quotechar='"')
        yield from rows

def create_headers(file_name):
    r_headers = next(read_data(file_name))
    headers = namedtuple(file_name.split('.')[0].title(), r_headers)
    return headers

def data_parse(file_name):
    rows = read_data(file_name)
    # names = create_headers(file_name)
    next(rows)
    combined_rows = (zip(row, data_types_file[file_name]) for row in rows)
    data = (data_types_parse(item) for item in combined_rows)
    yield from data

def data_correction(value, data_type):
    if data_type == 'INT':
        return int(value)
    elif data_type == 'DATE':
        d = value.strip('Z').split('T')
        d1 = [int(i) for i in d[0].split('-')]
        d2 = [int(i) for i in d[1].split(':')]
        return datetime(*list(chain(d1,d2)))
    else:
        return str(value)

def data_types_parse(row):
    return (data_correction(value, data_type) for value, data_type in row)

def headers_combine():
    combined_headers = []
    for item in data_types_file.keys():
        r_headers = next(read_data(item))
        for elem in r_headers:
            if elem not in combined_headers:
                combined_headers.append(elem)
    return combined_headers

def merged_iter(iters):
    pars = zip(*iters)
    rows = (chain.from_iterable(row) for row in pars)
    compressed_rows = (compress(row, data_bools) for row in rows)
    return compressed_rows

def merged_named_tuple(compressed_rows):
    headers_name = namedtuple('Person', all_headers)
    data = (headers_name(*row) for row in compressed_rows)
    return data

def stale_records(data, date, fmt='%m/%d/%Y'):
    r_date = datetime.strptime(date, fmt)
    stale_rec = (item for item in data if item.last_updated > r_date)
    return stale_rec

def group_genders(data, gender):
    sorted_data = sorted((row for row in data if row.gender == gender), key=lambda x: x.vehicle_make)
    grouped = groupby(sorted_data, key=lambda x: x.vehicle_make)
    group_counts = ((g[0], len(list(g[1]))) for g in grouped)
    return sorted(group_counts, key=lambda row: row[1], reverse=True)

all_headers = headers_combine()

personal_info = data_parse('personal_info.csv')
employment_data = data_parse('employment.csv')
update_status = data_parse('update_status.csv')
vehicles = data_parse('vehicles.csv')

parsers = personal_info, employment_data, update_status, vehicles

n = merged_named_tuple(merged_iter(parsers))

# d = stale_records(n, '3/1/2017')
m = 'Male'
f = 'Female'
l = group_genders(n, f)

for i in range(5):
    print(l[i])


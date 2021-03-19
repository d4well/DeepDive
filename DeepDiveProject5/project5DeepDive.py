import csv
from collections import namedtuple
from itertools import islice

def get_dialect(file_name):
    with open(file_name) as f:
            sample = f.read(1000)
            dialect = csv.Sniffer().sniff(sample)
    return dialect

class CsvFileManager:
    def __init__(self, file_name):
        self.file_name = file_name
        self._seek = 0
        self._read_head = 0

    def seek(self, value):
        self._seek = value

    def __enter__(self):
        self._file = open(self.file_name, 'r')
        self._read = csv.reader(self._file, get_dialect(self.file_name))
        headers = map(lambda x: x.lower(), next(self._read))
        self._nr = namedtuple('Data', headers)
        return self
    
    def __exit__(self, exc_type, exc_value, exc_trace):
        self._file.close()
        return False
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._file.closed:
            raise StopIteration
        else:
            return self._nr(*next(self._read))


with CsvFileManager('personal_info.csv') as f:
    for i in islice(f, 5):
        print(i)
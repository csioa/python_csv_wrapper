import csv
from collections import namedtuple


class FileWrapper:

    def __init__(self):
        self._file_path = "csv_files/mock_data.csv"

        with open(self._file_path, 'r') as filename:
            reader = csv.reader(filename)
            self._Profile = namedtuple('Profile', ' '.join(next(reader, None)))

    def file_to_namedtuple(self):

        with open(self._file_path, 'r') as filename:
            reader = csv.reader(filename)
            return map(self._Profile._make, reader)


if __name__ == '__main__':

    file_wrapper = FileWrapper()

    # Printing first row of CSV file as sample namedtuple
    print file_wrapper.file_to_namedtuple()[0]

    

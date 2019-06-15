import csv
from collections import namedtuple


class FileWrapper:

    def __init__(self, file_path):
        self._file_path = file_path

        with open(self._file_path, 'r') as filename:
            reader = csv.reader(filename)
            self._Profile = namedtuple('Profile', ' '.join(next(reader, None)))

    def file_to_namedtuple(self):

        with open(self._file_path, 'r') as filename:
            reader = csv.reader(filename)
            return map(self._Profile._make, reader)

    def get_headers(self):
        return list(self._Profile._fields)


if __name__ == '__main__':

    fw = FileWrapper("csv_files/mock_data.csv")

    # Getting a list of the headers of the file
    print (fw.get_headers())

    # Printing first row of CSV file as sample namedtuple
    print (fw.file_to_namedtuple()[0])

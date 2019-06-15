import csv
from collections import namedtuple


class FileConverter:

    def __init__(self, file_path):
        """
        :param file_path: the path to access the CSV file that the FileConverter should covnert
        :type file_path: string
        """
        self._file_path = file_path

        with open(self._file_path, 'r') as filename:
            reader = csv.reader(filename)
            self._Row = namedtuple('Row', ' '.join(next(reader, None)))

        self._headers = list(self._Row._fields)

    def get_filename(self):
        return self._file_path

    def get_headers(self):
        """
        :return: list of headers from the given CSV file
        """
        return self._headers

    def file_to_namedtuple(self, with_headers=True):
        """
        :param with_headers: true if the returned iterable should contain the heards - false otherwise
        :type with_headers: boolean
        :return: list of Rows - every Row wraps on row of the CSV file
        """
        with open(self._file_path, 'r') as filename:
            reader = csv.reader(filename)
            if not with_headers:
                next(reader, None)

            return map(self._Row._make, reader)

    # def write_new_csv(self, file_path, headers, data):

    def file_to_dict_list(self):
        """
        :return: returns a list of dictionaries, where every element contains the values of a single row
        together with the respective keys
        """
        csv_dict_list = []

        with open(self._file_path, 'r') as filename:
            reader = csv.reader(filename)
            next(reader, None)
            for row in reader:
                csv_dict_list.append(dict(zip(self._headers, row)))

        return csv_dict_list

    # def get_list(self):


if __name__ == '__main__':

    fr = FileConverter("csv_files/mock_data.csv")

    # Getting a list of the headers of the file
    print ("==========================================================================================="
           "===============================")
    print ("\n Reading CSV file {file}".format(file=fr.get_filename()))
    print ("\n========================================================================================="
           "=================================")
    print (" \n Headers\n")
    print (fr.get_headers())
    print ("\n========================================================================================="
           "=================================")
    print (" \n Sample output for CSV to namedtuple - first 5 elements\n")
    for r in fr.file_to_namedtuple(False)[:5]:
        print "{fn} {ln} with ID = {id}, lives in {city}, {country}"\
            .format(fn=r.first_name, ln=r.last_name, id=r.id, city=r.city, country=r.country)
    print ("\n========================================================================================="
           "=================================")
    print (" \n Sample output for CSV to list of dictionaries - 1 element\n")
    for field, value in fr.file_to_dict_list()[0].items():
        print ("{field} : {value}".format(field=field, value=value))
    print ("\n========================================================================================="
           "=================================")
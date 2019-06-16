import csv
import os
from collections import namedtuple


class FileConverter:

    def __init__(self, file_path=""):
        """
        :param file_path: the path to access the CSV file that the FileConverter should covnert
        :type file_path: string
        """
        self._file_path = file_path
        self._file_exists = os.path.isfile(file_path)

        if self._file_exists:
            with open(self._file_path, 'r') as filename:
                reader = csv.reader(filename)
                self._Row = namedtuple('Row', ' '.join(next(reader, None)))

            self._headers = list(self._Row._fields)
        else:
            print("\n File not found!")

    def get_filename(self):
        return self._file_path

    def get_headers(self):
        """
        :return: list of headers from the given CSV file
        """
        headers = []
        if self._file_exists:
            headers = self._headers
        return headers

    def file_to_namedtuple(self, with_headers=True):
        """
        :param with_headers: true if the returned iterable should contain the heards - false otherwise
        :type with_headers: boolean
        :return: list of Rows - every Row wraps on row of the CSV file
        """
        namedtuple_list = []
        if self._file_exists:
            with open(self._file_path, 'r') as filename:
                reader = csv.reader(filename)
                if not with_headers:
                    next(reader, None)

                namedtuple_list = map(self._Row._make, reader)
        return namedtuple_list

    # def write_new_csv(self, file_path, headers, data):

    def file_to_dict_list(self):
        """
        :return: returns a list of dictionaries, where every element contains the values of a single row
        together with the respective keys
        """
        csv_dict_list = []
        if self._file_exists:
            with open(self._file_path, 'r') as filename:
                reader = csv.reader(filename)
                next(reader, None)
                for reader_row in reader:
                    csv_dict_list.append(dict(zip(self._headers, reader_row)))

        return csv_dict_list

    def file_to_list(self, with_headers=True):
        """
        :param with_headers: true if the returned iterable should contain the heards - false otherwise
        :type with_headers: boolean
        :return:
        """
        list_of_lists = []
        if self._file_exists:
            with open(self._file_path, 'r') as filename:
                reader = csv.reader(filename)
                if not with_headers:
                    next(reader, None)
                for reader_row in reader:
                    list_of_lists.append(reader_row)
        return list_of_lists


if __name__ == '__main__':

    fr = FileConverter("csv_files/payment_events_mock.csv")
    # fr = FileConverter("csv_files/customer_profile_mock.csv")

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
    for row in fr.file_to_namedtuple(False)[:5]:
        print row
    print ("\n========================================================================================="
           "=================================")
    print (" \n Sample output for CSV to list of dictionaries - 1 element\n")
    for row in fr.file_to_dict_list()[:1]:
        for field, value in row.items():
            print ("{field} : {value}".format(field=field, value=value))
    print ("\n========================================================================================="
           "=================================")
    print ("\n Sample output for CSV to list of lists - 5 elements\n")
    for row in fr.file_to_list(False)[:5]:
        print row
    print ("\n========================================================================================="
           "=================================")

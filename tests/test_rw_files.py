import unittest

from src.read_write_files import *
from src.merge_sort import *

class TestRWFiles(unittest.TestCase):
    def test_read_bin(self):
        array_random_numbers = []
        array_expected = [253161, 293217, 84591, 57084, 992328, 1438214,
        910653, 106848, 600246, 844451]
        with open ('randomnumbers.bin', 'rb') as file:
            for i in range(10):
                number = struct.unpack('i', file.read(4))[0]
                array_random_numbers.append(number)
            self.assertEqual(array_random_numbers,array_expected)

    def test_merge_sort(self):
        array_to_order = [8, 8, 7, 5, 3, 5, 1, 9, 2, 56]
        array_expected_asc = [1, 2, 3, 5, 5, 7, 8, 8, 9, 56]
        array_expected_des = [56, 9, 8, 8, 7, 5, 5, 3, 2, 1]

        array_ascending = mergeSort(array_to_order, ascending=True)
        self.assertEqual(array_ascending, array_expected_asc)
        array_descending = mergeSort(array_to_order, ascending=False)
        self.assertEqual(array_descending, array_expected_des)
        print(array_ascending)
        print(array_descending)


import unittest

from src.read_write_files import *
from src.merge_sort import *
from src.merge_sort import *
from src.heap_sort import *
from src.quick_sort_random import *
from src.insertion_sort import *
from src.insertion_sor_binary_search import *
from src.bubble_sort import *
from src.shell_sort import *
from src.comb_sort import *
from src.selection_sort import *
from src.merge_sort_count import *

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

    # def test_array_size(self):
    #     array_to_order = read_random_numbers()
    #     self.assertEqual(len(array_to_order), 10000000)
    #     array_ascending = mergeSort(array_to_order, ascending=True)
    #     self.assertEqual(len(array_ascending), 10000000)
    #     array_descending = mergeSort(array_to_order, ascending=False)
    #     self.assertEqual(len(array_descending), 10000000)


    def test_merge_sort(self):
        array_to_order = [8, 8, 7, 5, 3, 5, 1, 9, 2, 56]
        array_expected_asc = [1, 2, 3, 5, 5, 7, 8, 8, 9, 56]
        array_expected_des = [56, 9, 8, 8, 7, 5, 5, 3, 2, 1]

        array_ascending = mergeSort(array_to_order,ascending=True)
        self.assertEqual(array_ascending, array_expected_asc)
        array_descending = mergeSort(array_to_order, ascending=False)
        self.assertEqual(array_descending, array_expected_des)

    def test_heap_sort(self):
        array_to_order = [8, 8, 7, 5, 3, 5, 1, 9, 2, 56]
        array_expected = [1, 2, 3, 5, 5, 7, 8, 8, 9, 56]
        heap_sort(array_to_order)
        self.assertEqual(array_expected, array_to_order)

    def test_quick_sort_random(self):
        array_to_order = [8, 8, 7, 5, 3, 5, 1, 9, 2, 56]
        array_expected = [1, 2, 3, 5, 5, 7, 8, 8, 9, 56]
        comparacoes, trocas = inPlaceQuickSort(array_to_order,0,len(array_to_order)-1) 
        print('quiick', comparacoes, trocas)   
        self.assertEqual(array_expected, array_to_order)

    def test_insertion_sort(self):
        array_to_order = [8, 8, 7, 5, 3, 5, 1, 9, 2, 56]
        array_expected = [1, 2, 3, 5, 5, 7, 8, 8, 9, 56]
        array, comparacoes, trocas = insertionsort(array_to_order)
        print("insertion sort cmp trc ", comparacoes, trocas)
        self.assertEqual(array_expected, array_to_order)

    def test_insertion_sort_binary_search(self):
        array_to_order = [8, 8, 7, 5, 3, 5, 1, 9, 2, 56]
        array_expected = [1, 2, 3, 5, 5, 7, 8, 8, 9, 56]
        array_sorted, comparacoes, trocas = insertion_sort(array_to_order)
        print("insertion binary cmp trc", comparacoes, trocas)
        self.assertEqual(array_expected, array_sorted)

    def test_bubble_sort(self):
        array_to_order = [8, 8, 7, 5, 3, 5, 1, 9, 2, 56]
        array_expected = [1, 2, 3, 5, 5, 7, 8, 8, 9, 56]
        bubbleSort(array_to_order)
        self.assertEqual(array_expected, array_to_order)

    def test_shell_sort(self):
        array_to_order = [8, 8, 7, 5, 3, 5, 1, 9, 2, 56]
        array_expected = [1, 2, 3, 5, 5, 7, 8, 8, 9, 56]
        comparacoes, trocas = shellSort(array_to_order)
        print('shell sooort', comparacoes, trocas)
        self.assertEqual(array_expected, array_to_order)

    def test_comb_sort(self):
        array_to_order = [8, 8, 7, 5, 3, 5, 1, 9, 2, 56]
        array_expected = [1, 2, 3, 5, 5, 7, 8, 8, 9, 56]
        combSort(array_to_order)
        self.assertEqual(array_expected, array_to_order)

    def test_selection_sort(self):
        array_to_order = [8, 8, 7, 5, 3, 5, 1, 9, 2, 56]
        array_expected = [1, 2, 3, 5, 5, 7, 8, 8, 9, 56]
        comparacoes, trocas = selection_sort(array_to_order)
        print('selectioon', comparacoes, trocas)
        self.assertEqual(array_expected, array_to_order)

    # def test_merge_sort_count(self):
    #     array_to_order = [8, 8, 7, 5, 3, 5, 1, 9, 2, 56]
    #     array_expected = [1, 2, 3, 5, 5, 7, 8, 8, 9, 56]
    #     ordered_array, comparacoes = merge_sort(array_to_order, 0)
    #     print('comppp merge', comparacoes)
    #     self.assertEqual(array_expected, ordered_array)


    


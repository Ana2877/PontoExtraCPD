from src.read_write_files import *
from src.merge_sort import *
from random import randint

if __name__ == '__main__':
    array_radom = read_random_numbers()
    array_ascending = mergeSort(array_radom, ascending=True)
    array_descending = mergeSort(array_radom, ascending=False)


from src.read_write_files import *
from src.merge_sort import *

if __name__ == '__main__':
    array_radom = read_random_numbers()
    print(array_radom)
    array_ascending = mergeSort(array_radom, ascending=True)
    print(array_ascending)
    array_descending = mergeSort(array_radom, ascending=False)
    print(array_descending)


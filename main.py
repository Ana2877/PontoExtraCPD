from random import randint
import time
from src.read_write_files import *
from src.merge_sort import *
from sorts_action. bubble_sort import *
from sorts_action. comb_sort import *
from sorts_action.heap_sort import *

if __name__ == '__main__':
    #build the arrays
    f = open('saida.txt','w')
    array_radom = read_random_numbers()
    array_ascending = mergeSort(array_radom, ascending=True)
    array_descending = mergeSort(array_radom, ascending=False)

    #1000 elementos
    bubble_1000(array_radom, array_ascending, array_descending)
    comb_1000(array_radom, array_ascending, array_descending)
    heap_1000(array_radom, array_ascending, array_descending)

    #10000 elementos
    bubble_10000(array_radom, array_ascending, array_descending)
    comb_10000(array_radom, array_ascending, array_descending)
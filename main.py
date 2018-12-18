from random import randint
import time
from src.read_write_files import *
from src.merge_sort import *
from sorts_action. bubble_sort import *
from sorts_action. comb_sort import *
from sorts_action.heap_sort import *
from sorts_action.insertion_sort import *
from sorts_action.insertion_sort_binary import *
from sorts_action.selection_sort import *
from sorts_action.quick_sort import *
from sorts_action.shell_sort import *
from sorts_action.merge_sort import *

if __name__ == '__main__':
    #build the arrays
    f = open('saida.txt','w')
    array_radom = read_random_numbers()
    array_ascending, comparacoes = mergeSort(array_radom, 0, ascending=True)
    array_descending, comparacoes = mergeSort(array_radom, 0, ascending=False)

    #1000 elementos
    bubble_1000(array_radom, array_ascending, array_descending)
    comb_1000(array_radom, array_ascending, array_descending)
    heap_1000(array_radom, array_ascending, array_descending)
    insertion_1000(array_radom, array_ascending, array_descending)
    insertion_binary_1000(array_radom, array_ascending, array_descending)
    quick_1000(array_radom, array_ascending, array_descending)
    selection_1000(array_radom, array_ascending, array_descending)
    shell_1000(array_radom, array_ascending, array_descending)
    merge_1000(array_radom, array_ascending, array_descending)
    


    #10000 elementos
    bubble_10000(array_radom, array_ascending, array_descending)
    comb_10000(array_radom, array_ascending, array_descending)
    heap_10000(array_radom, array_ascending, array_descending)

    # #100000 elementos
    # heap_100000(array_radom, array_ascending, array_descending)

    # #1000000 elementos
    # heap_1000000(array_radom, array_ascending, array_descending)

    # #10000000 elementos
    # heap_10000000(array_radom, array_ascending, array_descending)
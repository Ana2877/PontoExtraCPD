from src.heap_sort import *
import time


def heap_1000(array_radom, array_ascending, array_descending):
    array_random_heap = array_radom[0:1000].copy()
    start_time = time.time()
    comparacoes, trocas = heap_sort(array_random_heap)
    print(array_random_heap)
    end_time = time.time() - start_time
    print(end_time)

    with open('saida.txt', 'a') as f:
        f.write('HepS, ' +'O, '+ '1000, ' + str(comparacoes)+ ', ' + str(trocas) +', ' +str(end_time) + '\n')


    #heap ascending
    array_ascending_heap = array_ascending[0:1000].copy()
    start_time = time.time()
    comparacoes, trocas = heap_sort(array_ascending_heap)
    print(array_ascending_heap[0:10])
    end_time = time.time() - start_time

    with open('saida.txt', 'a') as f:
        f.write('HepS, ' +'R, '+ '1000, ' + str(comparacoes)+ ', ' + str(trocas) +', ' +str(end_time) + '\n')


    #heap descending
    array_descending_heap = array_descending[0:1000].copy()
    start_time = time.time()
    comparacoes, trocas = heap_sort(array_descending_heap)
    print(array_descending_heap[0:10])
    end_time = time.time() - start_time
    with open('saida.txt', 'a') as f:
        f.write('HepS, ' +'I, '+ '1000, ' + str(comparacoes)+ ', ' + str(trocas) +', ' +str(end_time) + '\n')

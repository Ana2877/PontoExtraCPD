from src.heap_sort import *
import time


def heap_1000(array_radom, array_ascending, array_descending):
    array_random_heap = array_radom[0:1000].copy()
    start_time = time.time()
    comparacoes, trocas = heap_sort(array_random_heap)
    end_time = (time.time() - start_time)*1000

    with open('saida.txt', 'a') as f:
        f.write('HepS, ' +'R, '+ '1000, ' + str(trocas) +', ' + str(comparacoes)+ ', ' +str("{0:.2f}".format(end_time))  + '\n')


    #heap ascending
    array_ascending_heap = array_ascending[0:1000].copy()
    start_time = time.time()
    comparacoes, trocas = heap_sort(array_ascending_heap)
    end_time = (time.time() - start_time)*1000

    with open('saida.txt', 'a') as f:
        f.write('HepS, ' +'O, '+ '1000, ' + str(trocas) +', ' + str(comparacoes)+ ', ' +str("{0:.2f}".format(end_time))  + '\n')


    #heap descending
    array_descending_heap = array_descending[0:1000].copy()
    start_time = time.time()
    comparacoes, trocas = heap_sort(array_descending_heap)
    end_time = (time.time() - start_time)*1000
    with open('saida.txt', 'a') as f:
        f.write('HepS, ' +'I, '+ '1000, ' + str(trocas) +', ' + str(comparacoes)+ ', ' +str("{0:.2f}".format(end_time))  + '\n')

def heap_10000(array_radom, array_ascending, array_descending):
    array_random_heap = array_radom[0:10000].copy()
    start_time = time.time()
    comparacoes, trocas = heap_sort(array_random_heap)
    end_time = (time.time() - start_time)*1000
    with open('saida.txt', 'a') as f:
        f.write('HepS, ' +'R, '+ '10000, ' + str(trocas) +', ' + str(comparacoes)+ ', ' +str("{0:.2f}".format(end_time))  + '\n')


    #heap ascending
    array_ascending_heap = array_ascending[0:10000].copy()
    start_time = time.time()
    comparacoes, trocas = heap_sort(array_ascending_heap)
    end_time = (time.time() - start_time)*1000

    with open('saida.txt', 'a') as f:
        f.write('HepS, ' +'O, '+ '10000, ' + str(trocas) +', ' + str(comparacoes)+ ', ' +str("{0:.2f}".format(end_time))  + '\n')


    #heap descending
    array_descending_heap = array_descending[0:10000].copy()
    start_time = time.time()
    comparacoes, trocas = heap_sort(array_descending_heap)
    end_time = (time.time() - start_time)*1000
    with open('saida.txt', 'a') as f:
        f.write('HepS, ' +'I, '+ '10000, ' + str(trocas) +', ' + str(comparacoes)+ ', ' +str("{0:.2f}".format(end_time))  + '\n')


def heap_100000(array_radom, array_ascending, array_descending):
    array_random_heap = array_radom[0:100000].copy()
    start_time = time.time()
    comparacoes, trocas = heap_sort(array_random_heap)
    end_time = (time.time() - start_time)*1000
    with open('saida.txt', 'a') as f:
        f.write('HepS, ' +'R, '+ '100000, ' + str(trocas) +', ' + str(comparacoes)+ ', ' +str("{0:.2f}".format(end_time))  + '\n')


    #heap ascending
    array_ascending_heap = array_ascending[0:100000].copy()
    start_time = time.time()
    comparacoes, trocas = heap_sort(array_ascending_heap)
    end_time = (time.time() - start_time)*1000

    with open('saida.txt', 'a') as f:
        f.write('HepS, ' +'O, '+ '100000, ' + str(trocas) +', ' + str(comparacoes)+ ', ' +str("{0:.2f}".format(end_time))  + '\n')


    #heap descending
    array_descending_heap = array_descending[0:100000].copy()
    start_time = time.time()
    comparacoes, trocas = heap_sort(array_descending_heap)
    end_time = (time.time() - start_time)*1000
    with open('saida.txt', 'a') as f:
        f.write('HepS, ' +'I, '+ '100000, ' + str(trocas) +', ' + str(comparacoes)+ ', ' +str("{0:.2f}".format(end_time))  + '\n')


def heap_1000000(array_radom, array_ascending, array_descending):
    array_random_heap = array_radom[0:1000000].copy()
    start_time = time.time()
    comparacoes, trocas = heap_sort(array_random_heap)
    end_time = (time.time() - start_time)*1000
    with open('saida.txt', 'a') as f:
        f.write('HepS, ' +'R, '+ '1000000, ' + str(trocas) +', ' + str(comparacoes)+ ', ' +str("{0:.2f}".format(end_time))  + '\n')


    #heap ascending
    array_ascending_heap = array_ascending[0:1000000].copy()
    start_time = time.time()
    comparacoes, trocas = heap_sort(array_ascending_heap)
    end_time = (time.time() - start_time)*1000

    with open('saida.txt', 'a') as f:
        f.write('HepS, ' +'O, '+ '1000000, ' + str(trocas) +', ' + str(comparacoes)+ ', ' +str("{0:.2f}".format(end_time))  + '\n')


    #heap descending
    array_descending_heap = array_descending[0:1000000].copy()
    start_time = time.time()
    comparacoes, trocas = heap_sort(array_descending_heap)
    end_time = (time.time() - start_time)*1000
    with open('saida.txt', 'a') as f:
        f.write('HepS, ' +'I, '+ '1000000, ' + str(trocas) +', ' + str(comparacoes)+ ', ' +str("{0:.2f}".format(end_time))  + '\n')

def heap_10000000(array_radom, array_ascending, array_descending):
    array_random_heap = array_radom[0:10000000].copy()
    start_time = time.time()
    comparacoes, trocas = heap_sort(array_random_heap)
    end_time = (time.time() - start_time)*1000
    with open('saida.txt', 'a') as f:
        f.write('HepS, ' +'R, '+ '10000000, ' + str(trocas) +', ' + str(comparacoes)+ ', ' +str("{0:.2f}".format(end_time))  + '\n')


    #heap ascending
    array_ascending_heap = array_ascending[0:10000000].copy()
    start_time = time.time()
    comparacoes, trocas = heap_sort(array_ascending_heap)
    end_time = (time.time() - start_time)*1000

    with open('saida.txt', 'a') as f:
        f.write('HepS, ' +'O, '+ '10000000, ' + str(trocas) +', ' + str(comparacoes)+ ', ' +str("{0:.2f}".format(end_time))  + '\n')


    #heap descending
    array_descending_heap = array_descending[0:10000000].copy()
    start_time = time.time()
    comparacoes, trocas = heap_sort(array_descending_heap)
    end_time = (time.time() - start_time)*1000
    with open('saida.txt', 'a') as f:
        f.write('HepS, ' +'I, '+ '10000000, ' + str(trocas) +', ' + str(comparacoes)+ ', ' +str("{0:.2f}".format(end_time))  + '\n')


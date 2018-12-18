from src.quick_sort_random import *
import time


def quick_1000(array_radom, array_ascending, array_descending):
    array_random_quick = array_radom[0:1000].copy()
    start_time = time.time()
    comparacoes, trocas = inPlaceQuickSort(array_random_quick,0,len(array_random_quick)-1)
    print(array_random_quick)
    end_time = (time.time() - start_time)*1000

    with open('saida.txt', 'a') as f:
        f.write('QukS, ' +'R, '+ '1000, ' + str(trocas) +', ' + str(comparacoes)+ ', ' +str(end_time) + '\n')


    #quick ascending
    array_ascending_quick = array_ascending[0:1000].copy()
    start_time = time.time()
    comparacoes, trocas = inPlaceQuickSort(array_ascending_quick,0,len(array_ascending_quick)-1)
    end_time = (time.time() - start_time)*1000

    with open('saida.txt', 'a') as f:
        f.write('QukS, ' +'O, '+ '1000, ' + str(trocas) +', ' + str(comparacoes)+ ', ' +str(end_time) + '\n')


    #quick descending
    array_descending_quick = array_descending[0:1000].copy()
    start_time = time.time()
    comparacoes, trocas = inPlaceQuickSort(array_descending_quick,0,len(array_descending_quick)-1)
    end_time = (time.time() - start_time)*1000
    with open('saida.txt', 'a') as f:
        f.write('QukS, ' +'I, '+ '1000, ' + str(trocas) +', ' + str(comparacoes)+ ', ' +str(end_time) + '\n')

def quick_10000(array_radom, array_ascending, array_descending):
    array_random_quick = array_radom[0:10000].copy()
    start_time = time.time()
    comparacoes, trocas = inPlaceQuickSort(array_random_quick,0,len(array_random_quick)-1)
    end_time = (time.time() - start_time)*1000
    with open('saida.txt', 'a') as f:
        f.write('QukS, ' +'R, '+ '10000, ' + str(trocas) +', ' + str(comparacoes)+ ', ' +str(end_time) + '\n')


    #quick ascending
    array_ascending_quick = array_ascending[0:10000].copy()
    start_time = time.time()
    comparacoes, trocas = inPlaceQuickSort(array_ascending_quick,0,len(array_ascending_quick)-1)
    end_time = (time.time() - start_time)*1000

    with open('saida.txt', 'a') as f:
        f.write('QukS, ' +'O, '+ '10000, ' + str(trocas) +', ' + str(comparacoes)+ ', ' +str(end_time) + '\n')


    #quick descending
    array_descending_quick = array_descending[0:10000].copy()
    start_time = time.time()
    comparacoes, trocas = inPlaceQuickSort(array_descending_quick,0,len(array_descending_quick)-1)
    end_time = (time.time() - start_time)*1000
    with open('saida.txt', 'a') as f:
        f.write('QukS, ' +'I, '+ '10000, ' + str(trocas) +', ' + str(comparacoes)+ ', ' +str(end_time) + '\n')


def quick_100000(array_radom, array_ascending, array_descending):
    array_random_quick = array_radom[0:100000].copy()
    start_time = time.time()
    comparacoes, trocas = inPlaceQuickSort(array_random_quick,0,len(array_random_quick)-1)
    end_time = (time.time() - start_time)*1000
    with open('saida.txt', 'a') as f:
        f.write('QukS, ' +'R, '+ '100000, ' + str(trocas) +', ' + str(comparacoes)+ ', ' +str(end_time) + '\n')


    #quick ascending
    array_ascending_quick = array_ascending[0:100000].copy()
    start_time = time.time()
    comparacoes, trocas = inPlaceQuickSort(array_ascending_quick,0,len(array_ascending_quick)-1)
    end_time = (time.time() - start_time)*1000

    with open('saida.txt', 'a') as f:
        f.write('QukS, ' +'O, '+ '100000, ' + str(trocas) +', ' + str(comparacoes)+ ', ' +str(end_time) + '\n')


    #quick descending
    array_descending_quick = array_descending[0:100000].copy()
    start_time = time.time()
    comparacoes, trocas = inPlaceQuickSort(array_descending_quick,0,len(array_descending_quick)-1)
    end_time = (time.time() - start_time)*1000
    with open('saida.txt', 'a') as f:
        f.write('QukS, ' +'I, '+ '100000, ' + str(trocas) +', ' + str(comparacoes)+ ', ' +str(end_time) + '\n')


def quick_1000000(array_radom, array_ascending, array_descending):
    array_random_quick = array_radom[0:1000000].copy()
    start_time = time.time()
    comparacoes, trocas = inPlaceQuickSort(array_random_quick,0,len(array_random_quick)-1)
    end_time = (time.time() - start_time)*1000
    with open('saida.txt', 'a') as f:
        f.write('QukS, ' +'R, '+ '1000000, ' + str(trocas) +', ' + str(comparacoes)+ ', ' +str(end_time) + '\n')


    #quick ascending
    array_ascending_quick = array_ascending[0:1000000].copy()
    start_time = time.time()
    comparacoes, trocas = inPlaceQuickSort(array_ascending_quick,0,len(array_ascending_quick)-1)
    end_time = (time.time() - start_time)*1000

    with open('saida.txt', 'a') as f:
        f.write('QukS, ' +'O, '+ '1000000, ' + str(trocas) +', ' + str(comparacoes)+ ', ' +str(end_time) + '\n')


    #quick descending
    array_descending_quick = array_descending[0:1000000].copy()
    start_time = time.time()
    comparacoes, trocas = inPlaceQuickSort(array_descending_quick,0,len(array_descending_quick)-1)
    end_time = (time.time() - start_time)*1000
    with open('saida.txt', 'a') as f:
        f.write('QukS, ' +'I, '+ '1000000, ' + str(trocas) +', ' + str(comparacoes)+ ', ' +str(end_time) + '\n')

def quick_10000000(array_radom, array_ascending, array_descending):
    array_random_quick = array_radom[0:10000000].copy()
    start_time = time.time()
    comparacoes, trocas = inPlaceQuickSort(array_random_quick,0,len(array_random_quick)-1)
    end_time = (time.time() - start_time)*1000
    with open('saida.txt', 'a') as f:
        f.write('QukS, ' +'R, '+ '10000000, ' + str(trocas) +', ' + str(comparacoes)+ ', ' +str(end_time) + '\n')


    #quick ascending
    array_ascending_quick = array_ascending[0:10000000].copy()
    start_time = time.time()
    comparacoes, trocas = inPlaceQuickSort(array_ascending_quick,0,len(array_ascending_quick)-1)
    end_time = (time.time() - start_time)*1000

    with open('saida.txt', 'a') as f:
        f.write('QukS, ' +'O, '+ '10000000, ' + str(trocas) +', ' + str(comparacoes)+ ', ' +str(end_time) + '\n')


    #quick descending
    array_descending_quick = array_descending[0:10000000].copy()
    start_time = time.time()
    comparacoes, trocas = inPlaceQuickSort(array_descending_quick,0,len(array_descending_quick)-1)
    end_time = (time.time() - start_time)*1000
    with open('saida.txt', 'a') as f:
        f.write('QukS, ' +'I, '+ '10000000, ' + str(trocas) +', ' + str(comparacoes)+ ', ' +str(end_time) + '\n')


from src.merge_sort import *
import time


def merge_1000(array_radom, array_ascending, array_descending):
    array_random_merge = array_radom[0:1000].copy()
    start_time = time.time()
    array, comparacoes = mergeSort(array_random_merge, 0)

    end_time = (time.time() - start_time)*1000

    with open('saida.txt', 'a') as f:
        f.write('MerS, ' +'R, '+ '1000, ' + '0' +', ' + str(comparacoes)+ ', ' +str("{0:.2f}".format(end_time))  + '\n')


    #merge ascending
    array_ascending_merge = array_ascending[0:1000].copy()
    start_time = time.time()
    array, comparacoes = mergeSort(array_ascending_merge, 0)
    end_time = (time.time() - start_time)*1000

    with open('saida.txt', 'a') as f:
        f.write('MerS, ' +'O, '+ '1000, ' + '0' +', ' + str(comparacoes)+ ', ' +str("{0:.2f}".format(end_time))  + '\n')


    #merge descending
    array_descending_merge = array_descending[0:1000].copy()
    start_time = time.time()
    array, comparacoes = mergeSort(array_descending_merge, 0)
    end_time = (time.time() - start_time)*1000
    with open('saida.txt', 'a') as f:
        f.write('MerS, ' +'I, '+ '1000, ' + '0' +', ' + str(comparacoes)+ ', ' +str("{0:.2f}".format(end_time))  + '\n')

def merge_10000(array_radom, array_ascending, array_descending):
    array_random_merge = array_radom[0:10000].copy()
    start_time = time.time()
    array, comparacoes = mergeSort(array_random_merge, 0)
    end_time = (time.time() - start_time)*1000
    with open('saida.txt', 'a') as f:
        f.write('MerS, ' +'R, '+ '10000, ' + '0' +', ' + str(comparacoes)+ ', ' +str("{0:.2f}".format(end_time))  + '\n')


    #merge ascending
    array_ascending_merge = array_ascending[0:10000].copy()
    start_time = time.time()
    array, comparacoes = mergeSort(array_ascending_merge, 0)
    end_time = (time.time() - start_time)*1000

    with open('saida.txt', 'a') as f:
        f.write('MerS, ' +'O, '+ '10000, ' + '0' +', ' + str(comparacoes)+ ', ' +str("{0:.2f}".format(end_time))  + '\n')


    #merge descending
    array_descending_merge = array_descending[0:10000].copy()
    start_time = time.time()
    array, comparacoes = mergeSort(array_descending_merge, 0)
    end_time = (time.time() - start_time)*1000
    with open('saida.txt', 'a') as f:
        f.write('MerS, ' +'I, '+ '10000, ' + '0' +', ' + str(comparacoes)+ ', ' +str("{0:.2f}".format(end_time))  + '\n')


def merge_100000(array_radom, array_ascending, array_descending):
    array_random_merge = array_radom[0:100000].copy()
    start_time = time.time()
    array, comparacoes = mergeSort(array_random_merge, 0)
    end_time = (time.time() - start_time)*1000
    with open('saida.txt', 'a') as f:
        f.write('MerS, ' +'R, '+ '100000, ' + '0' +', ' + str(comparacoes)+ ', ' +str("{0:.2f}".format(end_time))  + '\n')


    #merge ascending
    array_ascending_merge = array_ascending[0:100000].copy()
    start_time = time.time()
    array, comparacoes = mergeSort(array_ascending_merge, 0)
    end_time = (time.time() - start_time)*1000

    with open('saida.txt', 'a') as f:
        f.write('MerS, ' +'O, '+ '100000, ' + '0' +', ' + str(comparacoes)+ ', ' +str("{0:.2f}".format(end_time))  + '\n')


    #merge descending
    array_descending_merge = array_descending[0:100000].copy()
    start_time = time.time()
    array, comparacoes = mergeSort(array_descending_merge, 0)
    end_time = (time.time() - start_time)*1000
    with open('saida.txt', 'a') as f:
        f.write('MerS, ' +'I, '+ '100000, ' + '0' +', ' + str(comparacoes)+ ', ' +str("{0:.2f}".format(end_time))  + '\n')


def merge_1000000(array_radom, array_ascending, array_descending):
    array_random_merge = array_radom[0:1000000].copy()
    start_time = time.time()
    array, comparacoes = mergeSort(array_random_merge, 0)
    end_time = (time.time() - start_time)*1000
    with open('saida.txt', 'a') as f:
        f.write('MerS, ' +'R, '+ '1000000, ' + '0' +', ' + str(comparacoes)+ ', ' +str("{0:.2f}".format(end_time))  + '\n')


    #merge ascending
    array_ascending_merge = array_ascending[0:1000000].copy()
    start_time = time.time()
    array, comparacoes = mergeSort(array_ascending_merge, 0)
    end_time = (time.time() - start_time)*1000

    with open('saida.txt', 'a') as f:
        f.write('MerS, ' +'O, '+ '1000000, ' + '0' +', ' + str(comparacoes)+ ', ' +str("{0:.2f}".format(end_time))  + '\n')


    #merge descending
    array_descending_merge = array_descending[0:1000000].copy()
    start_time = time.time()
    array, comparacoes = mergeSort(array_descending_merge, 0)
    end_time = (time.time() - start_time)*1000
    with open('saida.txt', 'a') as f:
        f.write('MerS, ' +'I, '+ '1000000, ' + '0' +', ' + str(comparacoes)+ ', ' +str("{0:.2f}".format(end_time))  + '\n')

def merge_10000000(array_radom, array_ascending, array_descending):
    array_random_merge = array_radom[0:10000000].copy()
    start_time = time.time()
    array, comparacoes = mergeSort(array_random_merge, 0)
    end_time = (time.time() - start_time)*1000
    with open('saida.txt', 'a') as f:
        f.write('MerS, ' +'R, '+ '10000000, ' + '0' +', ' + str(comparacoes)+ ', ' +str("{0:.2f}".format(end_time))  + '\n')


    #merge ascending
    array_ascending_merge = array_ascending[0:10000000].copy()
    start_time = time.time()
    array, comparacoes = mergeSort(array_ascending_merge, 0)
    end_time = (time.time() - start_time)*1000

    with open('saida.txt', 'a') as f:
        f.write('MerS, ' +'O, '+ '10000000, ' + '0' +', ' + str(comparacoes)+ ', ' +str("{0:.2f}".format(end_time))  + '\n')


    #merge descending
    array_descending_merge = array_descending[0:10000000].copy()
    start_time = time.time()
    array, comparacoes = mergeSort(array_descending_merge, 0)
    end_time = (time.time() - start_time)*1000
    with open('saida.txt', 'a') as f:
        f.write('MerS, ' +'I, '+ '10000000, ' + '0' +', ' + str(comparacoes)+ ', ' +str("{0:.2f}".format(end_time))  + '\n')


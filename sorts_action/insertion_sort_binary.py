from src.insertion_sor_binary_search import *
import time


def insertion_binary_1000(array_radom, array_ascending, array_descending):
    array_random_insertion_binary = array_radom[0:1000].copy()
    array, comparacoes, trocas, end_time = insertion_sort(array_random_insertion_binary)
    with open('saida.txt', 'a') as f:
        f.write('ISBB, ' +'R, '+ '1000, '  + str(trocas) +', ' + str(comparacoes)+ ', ' +str(end_time) + '\n')

    #insertion_binary ascending
    array_ascending_insertion_binary = array_ascending[0:1000].copy()
    array, comparacoes, trocas, end_time = insertion_sort(array_ascending_insertion_binary)
    with open('saida.txt', 'a') as f:
        f.write('ISBB, ' +'O, '+ '1000, '  + str(trocas) +', ' + str(comparacoes)+ ', ' +str(end_time)+ '\n')

    #insertion_binary descending
    array_descending_insertion_binary = array_descending[0:1000].copy()
    array, comparacoes, trocas, end_time = insertion_sort(array_descending_insertion_binary)
    with open('saida.txt', 'a') as f:
        f.write('ISBB, ' +'I, '+ '1000, '  + str(trocas) +', ' + str(comparacoes)+ ', ' +str(end_time)+ '\n')


def insertion_binary_10000(array_radom, array_ascending, array_descending):
    array_random_insertion_binary = array_radom[0:10000].copy()
    array, comparacoes, trocas, end_time = insertion_sort(array_random_insertion_binary)
    with open('saida.txt', 'a') as f:
        f.write('ISBB, ' +'R, '+ '10000, '  + str(trocas) +', ' + str(comparacoes)+ ', ' +str(end_time) + '\n')

    #insertion_binary ascending
    array_ascending_insertion_binary = array_ascending[0:10000].copy()
    array, comparacoes, trocas, end_time = insertion_sort(array_ascending_insertion_binary)
    with open('saida.txt', 'a') as f:
        f.write('ISBB, ' +'O, '+ '10000, '  + str(trocas) +', ' + str(comparacoes)+ ', ' +str(end_time)+ '\n')

    #insertion_binary descending
    array_descending_insertion_binary = array_descending[0:10000].copy()
    array, comparacoes, trocas, end_time = insertion_sort(array_descending_insertion_binary)
    with open('saida.txt', 'a') as f:
        f.write('ISBB, ' +'I, '+ '10000, '  + str(trocas) +', ' + str(comparacoes)+ ', ' +str(end_time)+ '\n')




def insertion_binary_100000(array_radom, array_ascending, array_descending):
    array_random_insertion_binary = array_radom[0:100000].copy()
    array, comparacoes, trocas, end_time = insertion_sort(array_random_insertion_binary)
    with open('saida.txt', 'a') as f:
        f.write('ISBB, ' +'R, '+ '100000, '  + str(trocas) +', ' + str(comparacoes)+ ', ' +str(end_time) + '\n')

    #insertion_binary ascending
    array_ascending_insertion_binary = array_ascending[0:100000].copy()
    array, comparacoes, trocas, end_time = insertion_sort(array_ascending_insertion_binary)
    with open('saida.txt', 'a') as f:
        f.write('ISBB, ' +'O, '+ '100000, '  + str(trocas) +', ' + str(comparacoes)+ ', ' +str(end_time)+ '\n')

    #insertion_binary descending
    array_descending_insertion_binary = array_descending[0:100000].copy()
    array, comparacoes, trocas, end_time = insertion_sort(array_descending_insertion_binary)
    with open('saida.txt', 'a') as f:
        f.write('ISBB, ' +'I, '+ '100000, '  + str(trocas) +', ' + str(comparacoes)+ ', ' +str(end_time)+ '\n')

def insertion_binary_1000000(array_radom, array_ascending, array_descending):
    array_random_insertion_binary = array_radom[0:1000000].copy()
    array, comparacoes, trocas, end_time = insertion_sort(array_random_insertion_binary)
    with open('saida.txt', 'a') as f:
        f.write('ISBB, ' +'R, '+ '1000000, '  + str(trocas) +', ' + str(comparacoes)+ ', ' +str(end_time) + '\n')

    #insertion_binary ascending
    array_ascending_insertion_binary = array_ascending[0:1000000].copy()
    array, comparacoes, trocas, end_time = insertion_sort(array_ascending_insertion_binary)
    with open('saida.txt', 'a') as f:
        f.write('ISBB, ' +'O, '+ '1000000, '  + str(trocas) +', ' + str(comparacoes)+ ', ' +str(end_time)+ '\n')

    #insertion_binary descending
    array_descending_insertion_binary = array_descending[0:100000].copy()
    array, comparacoes, trocas, end_time = insertion_sort(array_descending_insertion_binary)
    with open('saida.txt', 'a') as f:
        f.write('ISBB, ' +'I, '+ '1000000, '  + str(trocas) +', ' + str(comparacoes)+ ', ' +str(end_time)+ '\n')

def insertion_binary_10000000(array_radom, array_ascending, array_descending):
    array_random_insertion_binary = array_radom[0:1000000].copy()
    array, comparacoes, trocas, end_time = insertion_sort(array_random_insertion_binary)
    with open('saida.txt', 'a') as f:
        f.write('ISBB, ' +'R, '+ '1000000, '  + str(trocas) +', ' + str(comparacoes)+ ', ' +str(end_time) + '\n')

    #insertion_binary ascending
    array_ascending_insertion_binary = array_ascending[0:1000000].copy()
    array, comparacoes, trocas, end_time = insertion_sort(array_ascending_insertion_binary)
    with open('saida.txt', 'a') as f:
        f.write('ISBB, ' +'O, '+ '1000000, '  + str(trocas) +', ' + str(comparacoes)+ ', ' +str(end_time)+ '\n')

    #insertion_binary descending
    array_descending_insertion_binary = array_descending[0:1000000].copy()
    array, comparacoes, trocas, end_time = insertion_sort(array_descending_insertion_binary)
    with open('saida.txt', 'a') as f:
        f.write('ISBB, ' +'I, '+ '1000000, '  + str(trocas) +', ' + str(comparacoes)+ ', ' +str(end_time)+ '\n')

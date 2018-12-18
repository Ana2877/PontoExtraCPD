from src.insertion_sort import *
import time


def insertion_1000(array_radom, array_ascending, array_descending):
    array_random_insertion = array_radom[0:1000].copy()
    array, comparacoes, trocas, end_time = insertionsort(array_random_insertion)
    print(array_random_insertion)
    with open('saida.txt', 'a') as f:
        f.write('ISBL, ' +'R, '+ '1000, '  + str(trocas) +', ' + str(comparacoes)+ ', ' +str(end_time) + '\n')

    #insertion ascending
    array_ascending_insertion = array_ascending[0:1000].copy()
    array, comparacoes, trocas, end_time = insertionsort(array_ascending_insertion)
    with open('saida.txt', 'a') as f:
        f.write('ISBL, ' +'O, '+ '1000, '  + str(trocas) +', ' + str(comparacoes)+ ', ' +str(end_time)+ '\n')

    #insertion descending
    array_descending_insertion = array_descending[0:1000].copy()
    array, comparacoes, trocas, end_time = insertionsort(array_descending_insertion)
    with open('saida.txt', 'a') as f:
        f.write('ISBL, ' +'I, '+ '1000, '  + str(trocas) +', ' + str(comparacoes)+ ', ' +str(end_time)+ '\n')


def insertion_10000(array_radom, array_ascending, array_descending):
    array_random_insertion = array_radom[0:10000].copy()
    array, comparacoes, trocas, end_time = insertionsort(array_random_insertion)
    with open('saida.txt', 'a') as f:
        f.write('ISBL, ' +'R, '+ '10000, '  + str(trocas) +', ' + str(comparacoes)+ ', ' +str(end_time) + '\n')

    #insertion ascending
    array_ascending_insertion = array_ascending[0:10000].copy()
    array, comparacoes, trocas, end_time = insertionsort(array_ascending_insertion)
    with open('saida.txt', 'a') as f:
        f.write('ISBL, ' +'O, '+ '10000, '  + str(trocas) +', ' + str(comparacoes)+ ', ' +str(end_time)+ '\n')

    #insertion descending
    array_descending_insertion = array_descending[0:10000].copy()
    array, comparacoes, trocas, end_time = insertionsort(array_descending_insertion)
    with open('saida.txt', 'a') as f:
        f.write('ISBL, ' +'I, '+ '10000, '  + str(trocas) +', ' + str(comparacoes)+ ', ' +str(end_time)+ '\n')




def insertion_100000(array_radom, array_ascending, array_descending):
    array_random_insertion = array_radom[0:100000].copy()
    array, comparacoes, trocas, end_time = insertionsort(array_random_insertion)
    with open('saida.txt', 'a') as f:
        f.write('ISBL, ' +'R, '+ '100000, '  + str(trocas) +', ' + str(comparacoes)+ ', ' +str(end_time) + '\n')

    #insertion ascending
    array_ascending_insertion = array_ascending[0:100000].copy()
    array, comparacoes, trocas, end_time = insertionsort(array_ascending_insertion)
    with open('saida.txt', 'a') as f:
        f.write('ISBL, ' +'O, '+ '100000, '  + str(trocas) +', ' + str(comparacoes)+ ', ' +str(end_time)+ '\n')

    #insertion descending
    array_descending_insertion = array_descending[0:100000].copy()
    array, comparacoes, trocas, end_time = insertionsort(array_descending_insertion)
    with open('saida.txt', 'a') as f:
        f.write('ISBL, ' +'I, '+ '100000, '  + str(trocas) +', ' + str(comparacoes)+ ', ' +str(end_time)+ '\n')

def insertion_1000000(array_radom, array_ascending, array_descending):
    array_random_insertion = array_radom[0:1000000].copy()
    array, comparacoes, trocas, end_time = insertionsort(array_random_insertion)
    with open('saida.txt', 'a') as f:
        f.write('ISBL, ' +'R, '+ '1000000, '  + str(trocas) +', ' + str(comparacoes)+ ', ' +str(end_time) + '\n')

    #insertion ascending
    array_ascending_insertion = array_ascending[0:1000000].copy()
    array, comparacoes, trocas, end_time = insertionsort(array_ascending_insertion)
    with open('saida.txt', 'a') as f:
        f.write('ISBL, ' +'O, '+ '1000000, '  + str(trocas) +', ' + str(comparacoes)+ ', ' +str(end_time)+ '\n')

    #insertion descending
    array_descending_insertion = array_descending[0:100000].copy()
    array, comparacoes, trocas, end_time = insertionsort(array_descending_insertion)
    with open('saida.txt', 'a') as f:
        f.write('ISBL, ' +'I, '+ '1000000, '  + str(trocas) +', ' + str(comparacoes)+ ', ' +str(end_time)+ '\n')

def insertion_10000000(array_radom, array_ascending, array_descending):
    array_random_insertion = array_radom[0:1000000].copy()
    array, comparacoes, trocas, end_time = insertionsort(array_random_insertion)
    with open('saida.txt', 'a') as f:
        f.write('ISBL, ' +'R, '+ '1000000, '  + str(trocas) +', ' + str(comparacoes)+ ', ' +str(end_time) + '\n')

    #insertion ascending
    array_ascending_insertion = array_ascending[0:1000000].copy()
    array, comparacoes, trocas, end_time = insertionsort(array_ascending_insertion)
    with open('saida.txt', 'a') as f:
        f.write('ISBL, ' +'O, '+ '1000000, '  + str(trocas) +', ' + str(comparacoes)+ ', ' +str(end_time)+ '\n')

    #insertion descending
    array_descending_insertion = array_descending[0:1000000].copy()
    array, comparacoes, trocas, end_time = insertionsort(array_descending_insertion)
    with open('saida.txt', 'a') as f:
        f.write('ISBL, ' +'I, '+ '1000000, '  + str(trocas) +', ' + str(comparacoes)+ ', ' +str(end_time)+ '\n')





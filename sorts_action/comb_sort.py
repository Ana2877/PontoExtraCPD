from src.comb_sort import *
import time

def comb_1000(array_radom, array_ascending, array_descending):
    array_random_comb = array_radom[0:1000].copy()
    comparacoes, trocas, end_time = combSort(array_random_comb)
    
    with open('saida.txt', 'a') as f:
        f.write('CbSt, ' +'R, '+ '1000, '  + str(trocas) +', ' + str(comparacoes)+ ', ' +str(end_time) + '\n')

    #comb ascending
    array_ascending_comb = array_ascending[0:1000].copy()
    comparacoes, trocas, end_time = combSort(array_ascending_comb)
    with open('saida.txt', 'a') as f:
        f.write('CbSt, ' +'O, '+ '1000, '  + str(trocas) +', ' + str(comparacoes)+ ', ' +str(end_time)+ '\n')

    #comb descending
    array_descending_comb = array_descending[0:1000].copy()
    comparacoes, trocas, end_time = combSort(array_descending_comb)
    with open('saida.txt', 'a') as f:
        f.write('CbSt, ' +'I, '+ '1000, '  + str(trocas) +', ' + str(comparacoes)+ ', ' +str(end_time)+ '\n')


def comb_10000(array_radom, array_ascending, array_descending):
    array_random_comb = array_radom[0:10000].copy()
    comparacoes, trocas, end_time = combSort(array_random_comb)
    with open('saida.txt', 'a') as f:
        f.write('CbSt, ' +'R, '+ '10000, '  + str(trocas) +', ' + str(comparacoes)+ ', ' +str(end_time) + '\n')

    #comb ascending
    array_ascending_comb = array_ascending[0:10000].copy()
    comparacoes, trocas, end_time = combSort(array_ascending_comb)
    with open('saida.txt', 'a') as f:
        f.write('CbSt, ' +'O, '+ '10000, '  + str(trocas) +', ' + str(comparacoes)+ ', ' +str(end_time)+ '\n')

    #comb descending
    array_descending_comb = array_descending[0:10000].copy()
    comparacoes, trocas, end_time = combSort(array_descending_comb)
    with open('saida.txt', 'a') as f:
        f.write('CbSt, ' +'I, '+ '10000, '  + str(trocas) +', ' + str(comparacoes)+ ', ' +str(end_time)+ '\n')




def comb_100000(array_radom, array_ascending, array_descending):
    array_random_comb = array_radom[0:100000].copy()
    comparacoes, trocas, end_time = combSort(array_random_comb)
    with open('saida.txt', 'a') as f:
        f.write('CbSt, ' +'R, '+ '100000, '  + str(trocas) +', ' + str(comparacoes)+ ', ' +str(end_time) + '\n')

    #comb ascending
    array_ascending_comb = array_ascending[0:100000].copy()
    comparacoes, trocas, end_time = combSort(array_ascending_comb)
    with open('saida.txt', 'a') as f:
        f.write('CbSt, ' +'O, '+ '100000, '  + str(trocas) +', ' + str(comparacoes)+ ', ' +str(end_time)+ '\n')

    #comb descending
    array_descending_comb = array_descending[0:100000].copy()
    comparacoes, trocas, end_time = combSort(array_descending_comb)
    with open('saida.txt', 'a') as f:
        f.write('CbSt, ' +'I, '+ '100000, '  + str(trocas) +', ' + str(comparacoes)+ ', ' +str(end_time)+ '\n')

def comb_1000000(array_radom, array_ascending, array_descending):
    array_random_comb = array_radom[0:1000000].copy()
    comparacoes, trocas, end_time = combSort(array_random_comb)
    with open('saida.txt', 'a') as f:
        f.write('CbSt, ' +'R, '+ '1000000, '  + str(trocas) +', ' + str(comparacoes)+ ', ' +str(end_time) + '\n')

    #comb ascending
    array_ascending_comb = array_ascending[0:1000000].copy()
    comparacoes, trocas, end_time = combSort(array_ascending_comb)
    with open('saida.txt', 'a') as f:
        f.write('CbSt, ' +'O, '+ '1000000, '  + str(trocas) +', ' + str(comparacoes)+ ', ' +str(end_time)+ '\n')

    #comb descending
    array_descending_comb = array_descending[0:100000].copy()
    comparacoes, trocas, end_time = combSort(array_descending_comb)
    with open('saida.txt', 'a') as f:
        f.write('CbSt, ' +'I, '+ '1000000, '  + str(trocas) +', ' + str(comparacoes)+ ', ' +str(end_time)+ '\n')

def comb_10000000(array_radom, array_ascending, array_descending):
    array_random_comb = array_radom[0:1000000].copy()
    comparacoes, trocas, end_time = combSort(array_random_comb)
    with open('saida.txt', 'a') as f:
        f.write('CbSt, ' +'R, '+ '1000000, '  + str(trocas) +', ' + str(comparacoes)+ ', ' +str(end_time) + '\n')

    #comb ascending
    array_ascending_comb = array_ascending[0:1000000].copy()
    comparacoes, trocas, end_time = combSort(array_ascending_comb)
    with open('saida.txt', 'a') as f:
        f.write('CbSt, ' +'O, '+ '1000000, '  + str(trocas) +', ' + str(comparacoes)+ ', ' +str(end_time)+ '\n')

    #comb descending
    array_descending_comb = array_descending[0:1000000].copy()
    comparacoes, trocas, end_time = combSort(array_descending_comb)
    with open('saida.txt', 'a') as f:
        f.write('CbSt, ' +'I, '+ '1000000, '  + str(trocas) +', ' + str(comparacoes)+ ', ' +str(end_time)+ '\n')


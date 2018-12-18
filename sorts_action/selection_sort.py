from src.selection_sort import *
import time


def selection_1000(array_radom, array_ascending, array_descending):
    array_random_selection = array_radom[0:1000].copy()
    comparacoes, trocas, end_time = selection_sort(array_random_selection)
    print(array_random_selection)
    with open('saida.txt', 'a') as f:
        f.write('SelS, ' +'R, '+ '1000, ' + str(trocas) +', ' + str(comparacoes)+ ', '  +str(end_time) + '\n')

    #selection ascending
    array_ascending_selection = array_ascending[0:1000].copy()
    comparacoes, trocas, end_time = selection_sort(array_ascending_selection)
    with open('saida.txt', 'a') as f:
        f.write('SelS, ' +'O, '+ '1000, ' + str(trocas) +', ' + str(comparacoes)+ ', ' +str(end_time)+ '\n')

    #selection descending
    array_descending_selection = array_descending[0:1000].copy()
    comparacoes, trocas, end_time = selection_sort(array_descending_selection)
    with open('saida.txt', 'a') as f:
        f.write('SelS, ' +'I, '+ '1000, ' + str(trocas) +', ' + str(comparacoes)+ ', ' +str(end_time)+ '\n')


def selection_10000(array_radom, array_ascending, array_descending):
    array_random_selection = array_radom[0:10000].copy()
    comparacoes, trocas, end_time = selection_sort(array_random_selection)
    with open('saida.txt', 'a') as f:
        f.write('SelS, ' +'R, '+ '10000, ' + str(trocas) +', ' + str(comparacoes)+ ', ' +str(end_time) + '\n')

    #selection ascending
    array_ascending_selection = array_ascending[0:10000].copy()
    comparacoes, trocas, end_time = selection_sort(array_ascending_selection)
    with open('saida.txt', 'a') as f:
        f.write('SelS, ' +'O, '+ '10000, ' + str(trocas) +', ' + str(comparacoes)+ ', ' +str(end_time)+ '\n')

    #selection descending
    array_descending_selection = array_descending[0:10000].copy()
    comparacoes, trocas, end_time = selection_sort(array_descending_selection)
    with open('saida.txt', 'a') as f:
        f.write('SelS, ' +'I, '+ '10000, ' + str(trocas) +', ' + str(comparacoes)+ ', ' +str(end_time)+ '\n')




def selection_100000(array_radom, array_ascending, array_descending):
    array_random_selection = array_radom[0:100000].copy()
    comparacoes, trocas, end_time = selection_sort(array_random_selection)
    with open('saida.txt', 'a') as f:
        f.write('SelS, ' +'R, '+ '100000, ' + str(trocas) +', ' + str(comparacoes)+ ', ' +str(end_time) + '\n')

    #selection ascending
    array_ascending_selection = array_ascending[0:100000].copy()
    comparacoes, trocas, end_time = selection_sort(array_ascending_selection)
    with open('saida.txt', 'a') as f:
        f.write('SelS, ' +'O, '+ '100000, ' + str(trocas) +', ' + str(comparacoes)+ ', ' +str(end_time)+ '\n')

    #selection descending
    array_descending_selection = array_descending[0:100000].copy()
    comparacoes, trocas, end_time = selection_sort(array_descending_selection)
    with open('saida.txt', 'a') as f:
        f.write('SelS, ' +'I, '+ '100000, ' + str(trocas) +', ' + str(comparacoes)+ ', ' +str(end_time)+ '\n')

def selection_1000000(array_radom, array_ascending, array_descending):
    array_random_selection = array_radom[0:1000000].copy()
    comparacoes, trocas, end_time = selection_sort(array_random_selection)
    with open('saida.txt', 'a') as f:
        f.write('SelS, ' +'R, '+ '1000000, ' + str(trocas) +', ' + str(comparacoes)+ ', ' +str(end_time) + '\n')

    #selection ascending
    array_ascending_selection = array_ascending[0:1000000].copy()
    comparacoes, trocas, end_time = selection_sort(array_ascending_selection)
    with open('saida.txt', 'a') as f:
        f.write('SelS, ' +'O, '+ '1000000, ' + str(trocas) +', ' + str(comparacoes)+ ', ' +str(end_time)+ '\n')

    #selection descending
    array_descending_selection = array_descending[0:100000].copy()
    comparacoes, trocas, end_time = selection_sort(array_descending_selection)
    with open('saida.txt', 'a') as f:
        f.write('SelS, ' +'I, '+ '1000000, ' + str(trocas) +', ' + str(comparacoes)+ ', ' +str(end_time)+ '\n')

def selection_10000000(array_radom, array_ascending, array_descending):
    array_random_selection = array_radom[0:1000000].copy()
    comparacoes, trocas, end_time = selection_sort(array_random_selection)
    with open('saida.txt', 'a') as f:
        f.write('SelS, ' +'R, '+ '1000000, ' + str(trocas) +', ' + str(comparacoes)+ ', ' +str(end_time) + '\n')

    #selection ascending
    array_ascending_selection = array_ascending[0:1000000].copy()
    comparacoes, trocas, end_time = selection_sort(array_ascending_selection)
    with open('saida.txt', 'a') as f:
        f.write('SelS, ' +'O, '+ '1000000, ' + str(trocas) +', ' + str(comparacoes)+ ', ' +str(end_time)+ '\n')

    #selection descending
    array_descending_selection = array_descending[0:1000000].copy()
    comparacoes, trocas, end_time = selection_sort(array_descending_selection)
    with open('saida.txt', 'a') as f:
        f.write('SelS, ' +'I, '+ '1000000, ' + str(trocas) +', ' + str(comparacoes)+ ', ' +str(end_time)+ '\n')




from src.bubble_sort import *
import time


def bubble_1000(array_radom, array_ascending, array_descending):
    array_random_bubble = array_radom[0:1000].copy()
    comparacoes, trocas, end_time = bubbleSort(array_random_bubble)
    with open('saida.txt', 'a') as f:
        f.write('BubS, ' +'R, '+ '1000, ' + str(comparacoes)+ ', ' + str(trocas) +', ' +str(end_time) + '\n')

    #bubble ascending
    array_ascending_bubble = array_ascending[0:1000].copy()
    comparacoes, trocas, end_time = bubbleSort(array_ascending_bubble)
    with open('saida.txt', 'a') as f:
        f.write('BubS, ' +'O, '+ '1000, ' + str(comparacoes)+ ', ' + str(trocas) +', ' +str(end_time)+ '\n')

    #bubble descending
    array_descending_bubble = array_descending[0:1000].copy()
    comparacoes, trocas, end_time = bubbleSort(array_descending_bubble)
    with open('saida.txt', 'a') as f:
        f.write('BubS, ' +'I, '+ '1000, ' + str(comparacoes)+ ', ' + str(trocas) +', ' +str(end_time)+ '\n')


def bubble_10000(array_radom, array_ascending, array_descending):
    array_random_bubble = array_radom[0:10000].copy()
    comparacoes, trocas, end_time = bubbleSort(array_random_bubble)
    with open('saida.txt', 'a') as f:
        f.write('BubS, ' +'R, '+ '10000, ' + str(comparacoes)+ ', ' + str(trocas) +', ' +str(end_time) + '\n')

    #bubble ascending
    array_ascending_bubble = array_ascending[0:10000].copy()
    comparacoes, trocas, end_time = bubbleSort(array_ascending_bubble)
    with open('saida.txt', 'a') as f:
        f.write('BubS, ' +'O, '+ '10000, ' + str(comparacoes)+ ', ' + str(trocas) +', ' +str(end_time)+ '\n')

    #bubble descending
    array_descending_bubble = array_descending[0:10000].copy()
    comparacoes, trocas, end_time = bubbleSort(array_descending_bubble)
    with open('saida.txt', 'a') as f:
        f.write('BubS, ' +'I, '+ '10000, ' + str(comparacoes)+ ', ' + str(trocas) +', ' +str(end_time)+ '\n')




def bubble_100000(array_radom, array_ascending, array_descending):
    array_random_bubble = array_radom[0:100000].copy()
    comparacoes, trocas, end_time = bubbleSort(array_random_bubble)
    with open('saida.txt', 'a') as f:
        f.write('BubS, ' +'R, '+ '100000, ' + str(comparacoes)+ ', ' + str(trocas) +', ' +str(end_time) + '\n')

    #bubble ascending
    array_ascending_bubble = array_ascending[0:100000].copy()
    comparacoes, trocas, end_time = bubbleSort(array_ascending_bubble)
    with open('saida.txt', 'a') as f:
        f.write('BubS, ' +'O, '+ '100000, ' + str(comparacoes)+ ', ' + str(trocas) +', ' +str(end_time)+ '\n')

    #bubble descending
    array_descending_bubble = array_descending[0:100000].copy()
    comparacoes, trocas, end_time = bubbleSort(array_descending_bubble)
    with open('saida.txt', 'a') as f:
        f.write('BubS, ' +'I, '+ '100000, ' + str(comparacoes)+ ', ' + str(trocas) +', ' +str(end_time)+ '\n')

def bubble_1000000(array_radom, array_ascending, array_descending):
    array_random_bubble = array_radom[0:1000000].copy()
    comparacoes, trocas, end_time = bubbleSort(array_random_bubble)
    with open('saida.txt', 'a') as f:
        f.write('BubS, ' +'R, '+ '1000000, ' + str(comparacoes)+ ', ' + str(trocas) +', ' +str(end_time) + '\n')

    #bubble ascending
    array_ascending_bubble = array_ascending[0:1000000].copy()
    comparacoes, trocas, end_time = bubbleSort(array_ascending_bubble)
    with open('saida.txt', 'a') as f:
        f.write('BubS, ' +'O, '+ '1000000, ' + str(comparacoes)+ ', ' + str(trocas) +', ' +str(end_time)+ '\n')

    #bubble descending
    array_descending_bubble = array_descending[0:100000].copy()
    comparacoes, trocas, end_time = bubbleSort(array_descending_bubble)
    with open('saida.txt', 'a') as f:
        f.write('BubS, ' +'I, '+ '1000000, ' + str(comparacoes)+ ', ' + str(trocas) +', ' +str(end_time)+ '\n')

def bubble_10000000(array_radom, array_ascending, array_descending):
    array_random_bubble = array_radom[0:1000000].copy()
    comparacoes, trocas, end_time = bubbleSort(array_random_bubble)
    with open('saida.txt', 'a') as f:
        f.write('BubS, ' +'R, '+ '1000000, ' + str(comparacoes)+ ', ' + str(trocas) +', ' +str(end_time) + '\n')

    #bubble ascending
    array_ascending_bubble = array_ascending[0:1000000].copy()
    comparacoes, trocas, end_time = bubbleSort(array_ascending_bubble)
    with open('saida.txt', 'a') as f:
        f.write('BubS, ' +'O, '+ '1000000, ' + str(comparacoes)+ ', ' + str(trocas) +', ' +str(end_time)+ '\n')

    #bubble descending
    array_descending_bubble = array_descending[0:1000000].copy()
    comparacoes, trocas, end_time = bubbleSort(array_descending_bubble)
    with open('saida.txt', 'a') as f:
        f.write('BubS, ' +'I, '+ '1000000, ' + str(comparacoes)+ ', ' + str(trocas) +', ' +str(end_time)+ '\n')






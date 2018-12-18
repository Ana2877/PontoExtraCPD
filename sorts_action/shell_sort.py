from src.shell_sort import *
import time


def shell_1000(array_radom, array_ascending, array_descending):
    array_random_shell = array_radom[0:1000].copy()
    comparacoes, trocas, end_time = shellSort(array_random_shell)
    with open('saida.txt', 'a') as f:
        f.write('SheS, ' +'R, '+ '1000, '  + str(trocas) +', ' + str(comparacoes)+ ', ' +str("{0:.2f}".format(end_time))  + '\n')

    #shell ascending
    array_ascending_shell = array_ascending[0:1000].copy()
    comparacoes, trocas, end_time = shellSort(array_ascending_shell)
    with open('saida.txt', 'a') as f:
        f.write('SheS, ' +'O, '+ '1000, '  + str(trocas) +', ' + str(comparacoes)+ ', ' +str("{0:.2f}".format(end_time)) + '\n')

    #shell descending
    array_descending_shell = array_descending[0:1000].copy()
    comparacoes, trocas, end_time = shellSort(array_descending_shell)
    with open('saida.txt', 'a') as f:
        f.write('SheS, ' +'I, '+ '1000, '  + str(trocas) +', ' + str(comparacoes)+ ', ' +str("{0:.2f}".format(end_time)) + '\n')


def shell_10000(array_radom, array_ascending, array_descending):
    array_random_shell = array_radom[0:10000].copy()
    comparacoes, trocas, end_time = shellSort(array_random_shell)
    with open('saida.txt', 'a') as f:
        f.write('SheS, ' +'R, '+ '10000, '  + str(trocas) +', ' + str(comparacoes)+ ', ' +str("{0:.2f}".format(end_time))  + '\n')

    #shell ascending
    array_ascending_shell = array_ascending[0:10000].copy()
    comparacoes, trocas, end_time = shellSort(array_ascending_shell)
    with open('saida.txt', 'a') as f:
        f.write('SheS, ' +'O, '+ '10000, '  + str(trocas) +', ' + str(comparacoes)+ ', ' +str("{0:.2f}".format(end_time)) + '\n')

    #shell descending
    array_descending_shell = array_descending[0:10000].copy()
    comparacoes, trocas, end_time = shellSort(array_descending_shell)
    with open('saida.txt', 'a') as f:
        f.write('SheS, ' +'I, '+ '10000, '  + str(trocas) +', ' + str(comparacoes)+ ', ' +str("{0:.2f}".format(end_time)) + '\n')




def shell_100000(array_radom, array_ascending, array_descending):
    array_random_shell = array_radom[0:100000].copy()
    comparacoes, trocas, end_time = shellSort(array_random_shell)
    with open('saida.txt', 'a') as f:
        f.write('SheS, ' +'R, '+ '100000, '  + str(trocas) +', ' + str(comparacoes)+ ', ' +str("{0:.2f}".format(end_time))  + '\n')

    #shell ascending
    array_ascending_shell = array_ascending[0:100000].copy()
    comparacoes, trocas, end_time = shellSort(array_ascending_shell)
    with open('saida.txt', 'a') as f:
        f.write('SheS, ' +'O, '+ '100000, '  + str(trocas) +', ' + str(comparacoes)+ ', ' +str("{0:.2f}".format(end_time)) + '\n')

    #shell descending
    array_descending_shell = array_descending[0:100000].copy()
    comparacoes, trocas, end_time = shellSort(array_descending_shell)
    with open('saida.txt', 'a') as f:
        f.write('SheS, ' +'I, '+ '100000, '  + str(trocas) +', ' + str(comparacoes)+ ', ' +str("{0:.2f}".format(end_time)) + '\n')

def shell_1000000(array_radom, array_ascending, array_descending):
    array_random_shell = array_radom[0:1000000].copy()
    comparacoes, trocas, end_time = shellSort(array_random_shell)
    with open('saida.txt', 'a') as f:
        f.write('SheS, ' +'R, '+ '1000000, '  + str(trocas) +', ' + str(comparacoes)+ ', ' +str("{0:.2f}".format(end_time))  + '\n')

    #shell ascending
    array_ascending_shell = array_ascending[0:1000000].copy()
    comparacoes, trocas, end_time = shellSort(array_ascending_shell)
    with open('saida.txt', 'a') as f:
        f.write('SheS, ' +'O, '+ '1000000, '  + str(trocas) +', ' + str(comparacoes)+ ', ' +str("{0:.2f}".format(end_time)) + '\n')

    #shell descending
    array_descending_shell = array_descending[0:100000].copy()
    comparacoes, trocas, end_time = shellSort(array_descending_shell)
    with open('saida.txt', 'a') as f:
        f.write('SheS, ' +'I, '+ '1000000, '  + str(trocas) +', ' + str(comparacoes)+ ', ' +str("{0:.2f}".format(end_time)) + '\n')

def shell_10000000(array_radom, array_ascending, array_descending):
    array_random_shell = array_radom[0:1000000].copy()
    comparacoes, trocas, end_time = shellSort(array_random_shell)
    with open('saida.txt', 'a') as f:
        f.write('SheS, ' +'R, '+ '1000000, '  + str(trocas) +', ' + str(comparacoes)+ ', ' +str("{0:.2f}".format(end_time))  + '\n')

    #shell ascending
    array_ascending_shell = array_ascending[0:1000000].copy()
    comparacoes, trocas, end_time = shellSort(array_ascending_shell)
    with open('saida.txt', 'a') as f:
        f.write('SheS, ' +'O, '+ '1000000, '  + str(trocas) +', ' + str(comparacoes)+ ', ' +str("{0:.2f}".format(end_time)) + '\n')

    #shell descending
    array_descending_shell = array_descending[0:1000000].copy()
    comparacoes, trocas, end_time = shellSort(array_descending_shell)
    with open('saida.txt', 'a') as f:
        f.write('SheS, ' +'I, '+ '1000000, '  + str(trocas) +', ' + str(comparacoes)+ ', ' +str("{0:.2f}".format(end_time)) + '\n')






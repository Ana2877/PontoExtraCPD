import time

def bubbleSort(arr):
    n = len(arr)
 
    start_time = time.time()
    comparacoes = 0
    trocas = 0
    for i in range(n):
        swap = False
        for j in range(0, n-i-1):
            comparacoes = comparacoes + 1
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
                trocas = trocas + 1
                swap = True
            if (time.time() - start_time) > 3600:
                break
        if swap == False:
            end_time = (time.time() - start_time)*1000
            return comparacoes, trocas, end_time
        if (time.time() - start_time) > 3600:
            end_time = '*'
            return comparacoes, trocas, end_time
    
    
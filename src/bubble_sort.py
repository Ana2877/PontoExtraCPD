def bubbleSort(arr):
    n = len(arr)
 
    comparacoes = 0
    trocas = 0
    for i in range(n):
        for j in range(0, n-i-1):
            comparacoes = comparacoes + 1
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
                trocas = trocas + 1

    return comparacoes, trocas
import time

def shellSort(arr): 

    n = len(arr) 
    gap = n//2
    comparacoes = 0
    trocas = 0
    start_time = time.time()
    while gap > 0: 
  
        for i in range(gap,n): 
            temp = arr[i] 

            j = i 
            comparacoes = comparacoes + 1
            while  j >= gap and arr[j-gap] >temp:
                trocas = trocas + 1
                arr[j] = arr[j-gap] 
                j -= gap  
            trocas = trocas + 1
            arr[j] = temp
        gap //= 2
        if (time.time() - start_time) > 3600:
            end_time = '*'
            return comparacoes, trocas, end_time
    end_time = (time.time() - start_time)*1000
    return comparacoes, trocas, end_time
import time

def getNextGap(gap): 
    gap = int((gap * 10)/13)
    if gap < 1:
        return 1
    return gap 

def combSort(arr): 
    comparacoes = 0
    trocas = 0
    start_time = time.time()
    n = len(arr) 
  
    gap = n 

    swapped = True
  
    while gap !=1 or swapped == 1: 
        gap = getNextGap(gap) 
        swapped = False

        for i in range(0, n-gap):
            comparacoes = comparacoes + 1
            if arr[i] > arr[i + gap]: 
                arr[i], arr[i + gap]=arr[i + gap], arr[i]
                trocas = trocas + 1
                swapped = True
            if (time.time() - start_time)>3600:
                return comparacoes, trocas, '*'   
    end_time = (time.time() - start_time)*1000
    return comparacoes, trocas, end_time
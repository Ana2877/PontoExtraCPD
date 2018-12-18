import time

def binary_search(arr, val, start, end, comparacoes): 
    if start == end:
        if arr[start] > val: 
            return start , comparacoes
        else: 
            return start+1, comparacoes

    if start > end: 
        return start , comparacoes
  
    mid = int((start+end)/2)
    comparacoes = comparacoes + 1
    if arr[mid] < val: 
        return binary_search(arr, val, mid+1, end, comparacoes)
    elif arr[mid] > val:
        comparacoes = comparacoes + 1
        return binary_search(arr, val, start, mid-1, comparacoes) 
    else: 
        comparacoes = comparacoes + 1
        return mid, comparacoes
  
def insertion_sort(arr):
    comparacoes = 0
    trocas = 0
    start_time = time.time()
    for i in range(1, len(arr)): 
        val = arr[i]
        j, comparacoes = binary_search(arr, val, 0, i-1, comparacoes) 
        arr = arr[:j] + [val] + arr[j:i] + arr[i+1:]
        trocas = trocas + abs(i-j)
        if(time.time() - start_time)>3600:
           return arr, comparacoes, trocas, '*'
    end_time = (time.time() - start_time)*1000
    return arr, comparacoes, trocas, end_time
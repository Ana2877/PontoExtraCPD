import time    

def selection_sort(A):
    comparacoes = 0
    trocas = 0
    start_time = time.time()
    for i in range(len(A)):
        min_idx = i
        for j in range(i+1, len(A)):
            comparacoes = comparacoes + 1
            if A[min_idx] > A[j]:
                min_idx = j
        trocas = trocas + 1        
        A[i], A[min_idx] = A[min_idx], A[i]
        if (time.time() - start_time) > 3600:
            end_time = '*'
            return comparacoes, trocas, end_time
    end_time = (time.time() - start_time)*1000
    return comparacoes, trocas, end_time
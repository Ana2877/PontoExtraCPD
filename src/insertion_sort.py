import time

def insertionsort(A):
    comparacoes = 0
    trocas = 0
    start_time = time.time()
    for j in range(1,len(A)):
        key = A[j]
        i = j-1
        
        comparacoes = comparacoes + 1
        while (i > -1) and key < A[i]: 
            A[i+1]=A[i]
            trocas = trocas + 1
            i=i-1
            comparacoes = comparacoes + 1
        if(i<=-1):
            comparacoes = comparacoes - 1
        A[i+1] = key
        if (time.time() - start_time) > 3600:
            return A, comparacoes, trocas, '*'
    end_time = (time.time() - start_time)*1000
    return A, comparacoes, trocas, end_time

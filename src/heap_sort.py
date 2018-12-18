def swap(i, j, sqc):                    
    sqc[i], sqc[j] = sqc[j], sqc[i] 

def heapify(end,i, sqc, comparacoes, trocas):   
    l=2 * i + 1  
    r=2 * (i + 1)   
    max=i
    comparacoes = comparacoes + 1
    if l < end and sqc[i] < sqc[l]:   
        max = l
    comparacoes = comparacoes + 1
    if r < end and sqc[max] < sqc[r]:   
        max = r   
    if max != i:
        trocas = trocas + 1
        swap(i, max, sqc)   
        heapify(end, max, sqc, comparacoes, trocas)
    return comparacoes, trocas 

def heap_sort(sqc):
    comparacoes = 0
    trocas = 0    
    end = len(sqc)   
    start = end // 2 - 1
    for i in range(start, -1, -1):   
        heapify(end, i, sqc, comparacoes, trocas) 
    for i in range(end-1, 0, -1):
        trocas = trocas + 1
        swap(i, 0, sqc)   
        comparacoes, trocas = heapify(i, 0, sqc, comparacoes, trocas)

    return comparacoes, trocas
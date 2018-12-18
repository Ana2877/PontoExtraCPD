    
def selection_sort(A):
    comparacoes = 0
    trocas = 0
    for i in range(len(A)):
        
        # Find the minimum element in remaining 
        # unsorted array
        min_idx = i
        for j in range(i+1, len(A)):
            comparacoes = comparacoes + 1
            if A[min_idx] > A[j]:
                min_idx = j
                
        # Swap the found minimum element with 
        # the first element
        trocas = trocas + 1        
        A[i], A[min_idx] = A[min_idx], A[i]
    return comparacoes, trocas
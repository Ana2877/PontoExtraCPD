def swap(i, j, sqc):                    
    sqc[i], sqc[j] = sqc[j], sqc[i] 

def heapify(end,i, sqc):   
    l=2 * i + 1  
    r=2 * (i + 1)   
    max=i   
    if l < end and sqc[i] < sqc[l]:   
        max = l   
    if r < end and sqc[max] < sqc[r]:   
        max = r   
    if max != i:   
        swap(i, max, sqc)   
        heapify(end, max, sqc)   

def heap_sort(sqc):     
    end = len(sqc)   
    start = end // 2 - 1
    for i in range(start, -1, -1):   
        heapify(end, i, sqc)   
    for i in range(end-1, 0, -1):   
        swap(i, 0, sqc)   
        heapify(i, 0, sqc)
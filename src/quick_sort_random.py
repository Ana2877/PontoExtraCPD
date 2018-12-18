from random import randint

def inPlaceQuickSort(A,start,end):
    if start<end:
        comparacoes = 0
        trocas = 0
        pivot=randint(start,end)
        trocas = trocas +1
        temp=A[end]
        A[end]=A[pivot]
        A[pivot]=temp
        
        p, comparacoes, trocas =inPlacePartition(A,start,end, comparacoes, trocas)
        inPlaceQuickSort(A,start,p-1)
        inPlaceQuickSort(A,p+1,end)
        return comparacoes, trocas


def inPlacePartition(A,start,end, comparacoes, trocas):
    pivot=randint(start,end)
    trocas = trocas +1
    temp=A[end]
    A[end]=A[pivot]
    A[pivot]=temp
    newPivotIndex=start-1
    for index in range(start,end):
        comparacoes = comparacoes + 1
        if A[index]<A[end]:#check if current val is less than pivot value
            trocas = trocas + 1
            newPivotIndex=newPivotIndex+1
            temp=A[newPivotIndex]
            A[newPivotIndex]=A[index]
            A[index]=temp
    trocas = trocas + 1
    temp=A[newPivotIndex+1]
    A[newPivotIndex+1]=A[end]
    A[end]=temp
    return newPivotIndex+1, comparacoes, trocas
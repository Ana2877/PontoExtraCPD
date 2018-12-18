def mergeSort(L, comparacoes, ascending = True):
    result = []  
    if len(L) == 1:
        return L, comparacoes
    mid = len(L) // 2

    teilliste1, comparacoes = mergeSort(L[:mid], comparacoes)

    teilliste2,comparacoes = mergeSort(L[mid:], comparacoes)

    x, y = 0, 0
    while x < len(teilliste1) and y < len(teilliste2):
        comparacoes = comparacoes + 1
        if teilliste1[x] > teilliste2[y]: # < for descending
            result.append(teilliste2[y])
            y = y + 1

        else:
            result.append(teilliste1[x])
            x = x + 1


    result = result + teilliste1[x:]

    result = result + teilliste2[y:]
    if ascending == True :
        return result, comparacoes
    else:
        result.reverse()
        return result, comparacoes
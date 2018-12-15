def mergeSort(L, ascending = True):
    result = []  
    if len(L) == 1:
        return L  
    mid = len(L) // 2

    teilliste1 = mergeSort(L[:mid])

    teilliste2 = mergeSort(L[mid:])

    x, y = 0, 0
    while x < len(teilliste1) and y < len(teilliste2):
        if teilliste1[x] > teilliste2[y]: # < for descending
            result.append(teilliste2[y])
            y = y + 1

        else:
            result.append(teilliste1[x])
            x = x + 1


    result = result + teilliste1[x:]

    result = result + teilliste2[y:]
    if ascending == True :
        return result
    else:
        result.reverse()
        return result
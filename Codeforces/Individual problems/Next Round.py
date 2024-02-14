x = [int(x) for x in input().split()]
scores = [int(y) for y in input().split()]

n, k = x[0], x[1]

if scores[k-1] > 0:
    cont = k
    if len(scores) > 1:
        i = k - 1
        j = i + 1
        salir = False
        while salir == False and j < n:
            if scores[j] == scores[i] and scores[j] != 0:
                j += 1
                cont += 1
            else:
                salir = True
else:
    if len(scores) > 1 and k != 1:
        i = k-1
        j = i - 1
        salir = False
        while salir == False and j > 0:
            if scores[i] == scores[j]:
                j -= 1
            else:
                salir = True
        if scores[j] != 0:
            cont = j+1
        else:
            cont = j
    elif len(scores) > 1 and k == 1:
        cont = 0
    else:
        cont = 0

print(cont)
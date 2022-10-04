

t = int(input())

for i in range(t):
    nk = [int(j) for j in input().split()]
    k = nk[1]
    a = [int(k) for k in input().split()]
    b = [int(s) for s in input().split()]
    for t in range(k):
        minimo, maximo = min(a), max(b)
        if minimo < maximo:
            a[a.index(minimo)] = maximo
            b[b.index(maximo)] = minimo
        else:
            continue
    print(sum(a))


n = int(input())

vec = []
for i in range(n):
    vec.append([int(j) for j in input().split()])

a = list(map(list, zip(*vec)))

def solucion(x, y):
    cont = 0
    for i in range(y):
        if sum(x[i]) != 0:
            return 'NO'
        else:
            cont += 1
        if cont == y:
            return 'YES'

print(solucion(a, len(a)))
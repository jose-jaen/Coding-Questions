from math import ceil

n, cont = int(input()), 0

lucky = [4, 7, 47, 74, 744, 477, 474, 747, 447, 777, 444]

for i in lucky:
    if n % i == 0:
        cont += 1

if cont == 0 and len(str(n)) == 2:
    k = str(n)
    if k[0] in ['4','7'] and k[1] in ['4', '7']:
        cont += 1
elif cont == 0 and len(str(n)) > 2:
    k = str(n)
    a = k[0:ceil(len(k)/2)-1]
    b = k[ceil(len(k)/2):len(k)]
    for i, j in zip(a, b):
        if i in ['4', '7'] and j in ['4', '7']:
            cont += 1

print('YES') if cont > 0 else print('NO')
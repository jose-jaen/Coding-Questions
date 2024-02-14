from statistics import mean

t = int(input())

for i in range(t):
    n = int(input())
    a = [int(j) for j in input().split()]
    suma = sum(a)
    if mean(a) == 1:
        print(0)
    elif n + 1 - suma > 0:
        print(1)
    else:
        print(suma - n)
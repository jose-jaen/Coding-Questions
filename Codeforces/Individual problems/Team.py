n = int(input())

cont = 0

for i in range(n):
    s = [int(j) for j in input().split()]
    if sum(s) >= 2:
        cont += 1

print(cont)
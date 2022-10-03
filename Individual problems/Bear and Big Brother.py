x = [int(x) for x in input().split()]

a, b = x[0], x[1]

cont = 0
while a <= b:
    a = 3*a
    b = 2*b
    cont += 1

print(cont)
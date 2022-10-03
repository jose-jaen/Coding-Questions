x = input()

i = 0
j = i + 1
cont = 1

while i < len(x) - 1 and cont < 7 and j < len(x):
    if x[i] == x[j]:
        cont += 1
        j += 1
    else:
        cont = 1
        i += 1
        j = i + 1

print('YES') if cont == 7 else print('NO')
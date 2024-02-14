n = int(input())

row = input()

i = 0
cont = 0

while i < len(row)-1:
    if row[i] == row[i + 1]:
        cont += 1
    i += 1

print(cont)
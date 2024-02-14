x = [int(s) for s in input().split()]

n, cont = x[0], x[1]

row = [t for t in input()]

positions = []

while cont > 0:
    for i in range(n - 1):
        if row[i] == 'B' and row[i + 1] == 'G':
            positions.append(i)
    for j in positions:
        row[j] = 'G'
        row[j + 1] = 'B'
    cont -= 1

print(''.join(row))
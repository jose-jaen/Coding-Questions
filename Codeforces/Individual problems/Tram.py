n = int(input())

info = []
for i in range(n):
    info.extend([int(j) for j in input().split()])

a, b = [], []
for i in range(len(info)):
    a.append(info[i]) if i % 2 == 0 else b.append(info[i])

p = a
p[0] = b[0]

for i in range(len(b)):
    if i != 0:
        p[i] = p[i - 1] + b[i] - a[i]

print(max(p))
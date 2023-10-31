data = []
s, n = [int(i) for i in input().split()]
for t in range(n):
    data.append([int(i) for i in input().split()])
data.sort(key=lambda x: x[0])
index = 0
fight = True
while fight and index < len(data):
    if s <= data[index][0]:
        fight = False
    else:
        s += data[index][1]
        index += 1
print('YES') if fight else print('NO')

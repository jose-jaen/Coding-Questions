a, b = input(), input()

res = []
for i in range(len(a)):
    res.append('1') if a[i] != b[i] else res.append('0')

print(''.join(res))
n = int(input())

res = []

i = 1
while i <= n-1:
    if i % 2 != 0:
        res.append('I hate that')
    else:
        res.append('I love that')
    i += 1

res.append('I hate it') if n % 2 != 0 else res.append('I love it')

print(' '.join(res))
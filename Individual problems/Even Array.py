from math import ceil

t = int(input())

for i in range(t):
    n = int(input())
    x = [int(j) for j in input().split()]
    ids = [s for s in range(len(x)) if x[s] % 2 != 0]
    res = [k for k in ids if k % 2 == 0]
    if len(x) % 2 == 0 and len(x) - len(ids) != len(x)/2:
        print(-1)
    elif len(x) % 2 != 0 and len(x) - len(ids) != ceil(len(x)/2) or (len(x) == 1 and x[0] %2 != 0):
        print(-1)
    else:
        print(len(res))

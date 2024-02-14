n, k = [int(i) for i in input().split()]
total = 5*n*(n + 1)/2 + k
while total > 240:
    n -= 1
    total = 5*n*(n+1)/2 + k
print(n)

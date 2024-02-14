n, m = [int(i) for i in input().split()]
     
i = 0
if n < m:
    print(n)
elif n == m:
    print(n+1)
else:
    while n >= 1:
        n -= 1
        i += 1
        if i%m == 0 and i != 1:
            n += 1
    print(i)
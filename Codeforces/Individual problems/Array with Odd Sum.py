t = int(input())
     
for i in range(t):
    n = int(input())
    a = [int(j) for j in input().split()]
    if sum(a) % 2 == 0:
        odd = [k for k in a if k % 2 != 0]
        print('YES') if len(a) - len(odd) != 0 and len(odd) > 1 else print('NO')
    else:
        print('YES')
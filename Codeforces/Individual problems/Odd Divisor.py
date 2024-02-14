t = int(input())
     
for i in range(t):
    n = int(input())
    print('YES') if n&(n-1) else print('NO')
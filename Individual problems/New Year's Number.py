t = int(input())
     
for i in range(t):
    n = int(input())
    y = n % 2020
    x = (n - y)/2020 - y
    print('YES') if x >= 0 else print('NO')
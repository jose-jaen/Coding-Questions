t = int(input())
for i in range(t):
    w, h, n = [int(j) for j in input().split()]
    print('YES') if ((w & -w) * (h & -h) >= n) else print('NO')
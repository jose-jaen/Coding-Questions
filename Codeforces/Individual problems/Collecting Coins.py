t = int(input())

for i in range(t):
    a, b, c, n = [int(j) for j in input().split()]
    sisters = [a, b, c]
    maximo = max(sisters)
    sisters = [maximo - i for i in sisters if i != maximo]
    resto = n - sum(sisters)
    print('YES') if resto % 3 == 0 and resto >= 0 else print('NO')

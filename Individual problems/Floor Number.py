t = int(input())

for i in range(t):
    n, x = [int(j) for j in input().split()]
    print(1 if n <= 2 else (n - 3) // x + 2)
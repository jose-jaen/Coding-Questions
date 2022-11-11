t = int(input())

for i in range(t):
    n = int(input())
    a = [int(j) for j in input().split()]
    print(max(a)-min(a))
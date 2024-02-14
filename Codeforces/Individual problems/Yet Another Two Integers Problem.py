from math import ceil
     
t = int(input())
     
for i in range(t):
    a, b = [int(j) for j in input().split()]
    res = b - a if b > a else a - b
    print(ceil(res/10))
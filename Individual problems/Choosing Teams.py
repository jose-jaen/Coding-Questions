from math import floor
     
n, k = [int(i) for i in input().split()]
     
teams = [int(j) for j in input().split()]
     
res = [i for i in teams if 5 - i >= k]
     
print(floor(len(res)/3))
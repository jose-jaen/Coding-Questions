

n, m = [int(i) for i in input().split()]
     
vec = sorted([int(j) for j in input().split()])
     
print(min(j - i for i, j in zip(vec, vec[n-1:])))


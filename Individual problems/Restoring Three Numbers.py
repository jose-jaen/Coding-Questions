vec = sorted([int(i) for i in input().split()])
     
c = max(vec) - vec[2]
b = vec[0] - c
a = max(vec) - b - c
     
print(a, b, c)
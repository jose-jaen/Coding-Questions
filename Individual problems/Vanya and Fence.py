x = [int(j) for j in input().split()]
     
n, h = x[0], x[1]
vec = [int(j) for j in input().split()]
w = len(vec)
     
for i in vec:
    if i > h:
        w += 1
     
print(w)
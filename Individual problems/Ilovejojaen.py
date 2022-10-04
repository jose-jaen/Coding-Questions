n = int(input())
vec = [int(j) for j in input().split()]
     
cont = 0
for i in range(1, n):
    if vec[i] > max(vec[:i]) or vec[i] < min(vec[:i]):
        cont += 1
     
print(cont)
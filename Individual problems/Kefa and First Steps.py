n = int(input())
x = [int(j) for j in input().split()]

i, cont = 0, 1
vec = []

while i < n-1:
    if x[i] <= x[i+1]:
        cont += 1
    else:
        vec.append(cont)
        cont = 1
    i += 1
    vec.append(cont)

print(max(vec)) if n > 1 else print(1)
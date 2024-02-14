x = []

for i in range(3):
    x.append(int(input()))

def solucion(a, b, c):
    vec = []
    vec.append(a * b * c)
    vec.append(a + b + c)
    vec.append((a + b) * c)
    vec.append(a * (b + c))
    vec.append(a + b * c)
    vec.append(a * b + c)
    return max(vec)

print(solucion(x[0], x[1], x[2]))
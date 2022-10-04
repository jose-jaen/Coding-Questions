n = int(input())
     
s = []
for i in range(n):
    s.extend([i for i in input().split()])
        
values = [4, 6, 8, 12, 20]
     
count = [s.count('Tetrahedron'), s.count('Cube'), s.count('Octahedron'),
        s.count('Dodecahedron'), s.count('Icosahedron')]
            
res = [i*j for i, j in zip(values, count)]
     
print(sum(res))
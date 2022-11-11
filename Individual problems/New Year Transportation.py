n, t = [int(i) for i in input().split()]
     
a = [0]
a.extend([int(i) for i in input().split()])
     
i = 1
while i < t:
    i += a[i]
     
print('YES') if i == t else print('NO')
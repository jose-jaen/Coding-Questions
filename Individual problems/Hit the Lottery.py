

n = int(input())
     
cont = 0
     
d = [100, 20, 10, 5, 1]
     
while n >= 1:
    i = 0
    while i < len(d):
        if n/d[i] >= 1:
            n -= d[i]
            cont += 1
        else: 
            i += 1
                
print(cont)


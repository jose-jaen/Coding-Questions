n = int(input())
     
vec = []
     
for i in range(n):
    x = [int(j) for j in input().split()]
    vec.extend(x)
        
home = [vec[j] for j in range(len(vec)) if j % 2 == 0]
guest = [vec[j] for j in range(len(vec)) if j % 2 != 0]
     
cont = 0
for i in home:
    cont += guest.count(i)
        
print(cont)
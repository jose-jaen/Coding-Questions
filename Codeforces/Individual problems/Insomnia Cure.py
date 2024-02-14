vec = []
     
for i in range(5):
    vec.append(int(input()))
        
d = vec[len(vec)-1]
     
comp = [j for j in vec[0:4] if j > d]
        
if len(comp) == 4:
    print(0)
elif 1 in vec[0:4]:
    print(d)
else:
    res = []
    for i in set(vec[0:4]):
        j = i
        while j <= d:
            res.append(j)
            j += i
    print(len(set(res)))
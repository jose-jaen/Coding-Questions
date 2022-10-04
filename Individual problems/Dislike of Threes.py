t = int(input())

info = []
for i in range(t):
    info.append(int(input()))
    
vec = []
i = 1
while len(vec) < max(info):
    if i % 3 != 0 and str(i)[len(str(i))-1] != '3':
        vec.append(i)
    else:
        j = i
        while j % 3 == 0 or str(j)[len(str(j))-1] == '3':
            j += 1
        vec.append(j)
    vec = [i for i in set(vec)]
    i += 1

for i in info:
    print(vec[i-1])
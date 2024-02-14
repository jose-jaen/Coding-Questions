x = input()
     
vec = []
for i in x:
    vec.append(i)
     
ids = []
for i in range(len(vec)-2):
    if vec[i] == 'W' and vec[i+1] == 'U' and vec[i+2] == 'B':
        vec[i] = ' '
        ids.append(i+1)
        ids.append(i+2)
     
vec = [vec[j] for j in range(len(x)) if j not in ids]
     
res = ''.join(vec)
     
res = res.replace("  ", " ")
     
if res[0] != ' ' and '  ' not in res:
    print(res)
elif res[0] == ' ' and '  ' not in res:
    print(res[1:len(res)])
elif res[0] == ' ' and '  ' in res:
    print(res[1:len(res)].strip())
elif res[0] != ' ' and '  ' in res:
    print(res.replace('  ' , ' '))
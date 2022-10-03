x = input().lower()

v = ['a', 'e', 'i', 'o', 'u']

for i in v: 
    x = x.replace(i, '')

res = []
for i in range(len(x)): 
    res.append('.' + x[i])  

print(''.join(res))
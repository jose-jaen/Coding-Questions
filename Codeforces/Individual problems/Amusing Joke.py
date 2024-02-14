guest = [i for i in input()]
host = [i for i in input()]
pile = [i for i in input()]
     
res = pile
     
for i in range(len(host)):
    if host[i] in pile:
        res.remove(host[i])
     
res.sort()
guest.sort()
     
print('YES') if res == guest else print('NO')

info = [int(i) for i in input().split()]
     
cont = 0
     
while 0 not in info:
    i = info.index(min(info))
    cont += 1
    info[i] -= 1
     
print('Akshat') if cont % 2 != 0 else print('Malvika')
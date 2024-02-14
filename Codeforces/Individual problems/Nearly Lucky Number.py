x = input()
     
cont = 0
for i in x:
    if i in ['4', '7']:
        cont += 1
            
print('YES') if cont in [4, 7] else print('NO')
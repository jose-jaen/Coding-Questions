x, j = input(), input()
     
cont = 0
for i in j:
    if i == 'A':
        cont += 1
            
print('Anton') if cont > int(x) - cont else print('Friendship') if cont == int(x)/2 else print('Danik')
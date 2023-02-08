program = input()

cont = 0
vec = ['H', 'Q', '9']
for i in program:
    if i in vec:
        cont += 1
    elif i in vec and '+' in vec:
        cont +=1
        
print('YES') if cont > 0 else print('NO')

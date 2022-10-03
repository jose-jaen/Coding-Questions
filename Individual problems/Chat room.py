word = 'hello'

x = input()

j, cont = 0, 0

for i in range(len(x)):
    if x[i] == word[j]:
        j += 1
    if j == 5:
        cont +=1
        break
     
print('YES') if cont == 1 else print('NO')
x = [int(j) for j in input().split()]
value = [int(j) for j in input().split()]

value.sort()
value = value[::-1]
     
cont, i = 0, 0
salir = False
while i < len(value) and salir == False:
    cont += value[i]
    resto = sum(value[(i+1):len(value)])
    if cont > resto:
        salir = True
    i += 1
        
print(i)
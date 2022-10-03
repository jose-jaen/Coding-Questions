a = input()
b = int(a)
     
salir = False
     
while salir == False:
    b += 1
    if len(set(str(b))) == len(a):
        salir = True
            
print(b)
y = 0
     
for i in range(int(input())):
    x = input()
    if '++' in x:
        y += 1
    else:
        y -= 1
            
print(y)
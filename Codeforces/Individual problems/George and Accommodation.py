cont = 0
 
for i in range(int(input())):
    x = [int(x) for x in input().split()]
    if x[1] - x[0] >= 2:
        cont += 1

print(cont)
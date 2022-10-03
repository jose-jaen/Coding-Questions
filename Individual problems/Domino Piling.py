from math import trunc

x = [int(i) for i in input().split()]

area = x[0]*x[1]

print(int(area/2)) if area % 2==0 else print(trunc(area/2))
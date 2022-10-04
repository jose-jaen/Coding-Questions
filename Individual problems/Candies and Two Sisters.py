

from math import floor
     
t = int(input())
     
for i in range(t):
    x = int(input())
    if x <= 2:
        print(0)
    else:
        print(floor(x/2)) if x % 2 != 0 else print(floor(x/2)-1)


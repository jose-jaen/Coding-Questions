from math import floor
     
socks = [int(i) for i in input().split()]
     
res = [str(min(socks)), str(floor((max(socks) - min(socks))/2))]
     
print(' '.join(res))

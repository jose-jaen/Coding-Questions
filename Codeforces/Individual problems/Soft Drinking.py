from math import floor
     
n, k, l, c, d, p, nl, np = [int(i) for i in input().split()]
     
liter, lime, salt = floor(k*l/nl), c*d,  floor(p/np)
     
res = floor(min(liter, lime, salt)/n)
     
print(res)
from math import ceil

n = int(input())
s = [int(i) for i in input().split()]

a, b = s.count(4), s.count(3)
c, d = s.count(2), s.count(1)

p = a + b

if d <= b:
    p += ceil(c/2)
else:
    p += ceil((d-b+2*c)/4)

print(p)
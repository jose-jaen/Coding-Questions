n = int(input())

m, c = 0 , 0

for i in range(n):
    x = [int(j) for j in input().split()]
    if x[0] > x[1]:
        m += 1
    elif x[0] < x[1]:
        c += 1
        
if m > c:
    print('Mishka')
elif m < c:
    print('Chris')
else:
    print('Friendship is magic!^^')
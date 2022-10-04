

t = int(input())
     
for i in range(t):
    x = [int(j) for j in input().split()]
    a, b = x[0], x[1]
    if a % b == 0:
        print(0)
    elif a < b:
        print(b-a)
    else:
        print(b - a%b)


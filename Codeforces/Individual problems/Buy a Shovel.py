k, r = [int(i) for i in input().split()]
x = 1
while k*x % 10 != 0 and k*x % 10 != r:
    x += 1
print(x)

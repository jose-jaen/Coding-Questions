x = [int(x) for x in input().split()]

k = x[0]
n = x[1]
w = x[2]
cost = k*w*(w+1)/2

print(round(abs(cost - n))) if cost > n else print(0)
n, m, a, b = [int(i) for i in input().split()]
if b / m < a:
    trips = n // m
    rest = n - m * trips
    print(b*trips + min(rest*a, b)) if trips else print(min(rest*a, b))
else:
    print(n*a)

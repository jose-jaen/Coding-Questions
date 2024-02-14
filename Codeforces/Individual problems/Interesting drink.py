import bisect
input()
x = sorted([int(i) for i in input().split()])
for i in ' ' * int(input()):
    print(bisect.bisect(x, int(input())))
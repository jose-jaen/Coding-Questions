t = int(input())

for i in range(t):
    h, m = [int(i) for i in input().split()]
    minutes = 60 - m if m != 0 else 0
    hours = 24 - h if minutes == 0 else 23 - h
    print(hours*60 + minutes)
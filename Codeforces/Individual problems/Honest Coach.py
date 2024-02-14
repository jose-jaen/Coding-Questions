t = int(input())
     
for i in range(t):
    n = int(input())
    s = sorted([int(j) for j in input().split()])
    difs = [s[i+1] - s[i] for i in range(n-1)]
    print(min(difs))
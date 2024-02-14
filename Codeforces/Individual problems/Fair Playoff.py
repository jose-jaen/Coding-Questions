t = int(input())
     
for i in range(t):
    s = [int(j) for j in input().split()]
    maxi, maxi2 = max(s), sorted(s)[2]
    round1, round2 = max(s[:2]), max(s[2:])
    cond1 = round1 not in [maxi, maxi2]
    cond2 = round2 not in [maxi, maxi2]
    print('NO') if cond1 or cond2 else print('YES')
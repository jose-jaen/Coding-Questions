t = int(input())
     
for j in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    res = [x for x in range(len(a)) if a.count(a[x]) == 1]
    print(res[0]+1)
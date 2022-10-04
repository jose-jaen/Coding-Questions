t = int(input())

for j in range(t):
    res = []
    n = int(input())
    task = input()
    for i in set(task):
        ids = [s for s in range(len(task)) if task[s] == i]
        res.extend(ids)
    res2 = res[:]
    res2.sort()
    print('NO') if res2 != res else print('YES')
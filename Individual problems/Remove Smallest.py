tests = int(input())
for test in range(tests):
    n = int(input())
    a = sorted([int(i) for i in input().split()], reverse=True)
    discard = True
    while discard and len(a) > 1:
        if abs(a[0] - a[1]) <= 1:
            del a[0]
        else:
            discard = False
    print('YES') if len(a) == 1 else print('NO')

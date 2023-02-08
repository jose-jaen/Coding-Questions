t = int(input())

for i in range(t):
    n = int(input())
    s = input()
    w = 'Timur'
    if len(set(s)) == 5 and len(s) == 5 and sorted(set(s)) == sorted(set(w)):
        print('YES')
    else:
        print('NO')

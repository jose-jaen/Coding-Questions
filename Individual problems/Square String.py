t = int(input())
for i in range(t):
    s = input()
    m = int(len(s)/2)
    print('YES') if s[:m] == s[m:] else print('NO')
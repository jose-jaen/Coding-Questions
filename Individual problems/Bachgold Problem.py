n = int(input())
     
count = 0
while n % 2 != 0:
    n -= 3
    count += 1
     
if n % 2 == 0:
    print(int(n/2) + count)
    a = [str(2)]*int(n/2)
    b = [str(3)]*count
    a.extend(b)
    print(' '.join(a))
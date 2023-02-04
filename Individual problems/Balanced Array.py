t = int(input())
     
for i in range(t):
    n = int(input())

    if n/2 % 2 != 0:
        print('NO')
     
    else:
        even = [j for j in range(1, n + 1) if j % 2 == 0]
        odd = [j for j in range(1, n) if j % 2 != 0]
        odd[len(odd) - 1] = sum(even) - sum(odd[:-1])
          
        if odd[len(odd) - 1] % 2 == 0:
            print('NO')
               
        else:
            even.extend(odd)
            even = [str(i) for i in even]
            print('YES')
            print(' '.join(even))

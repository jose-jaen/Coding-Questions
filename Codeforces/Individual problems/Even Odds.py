input = [int(j) for j in input().split()]

n = input[0]
k = input[1]

if n % 2 != 0 and k <= (n+1)/2:
    res = 2*k-1
elif n % 2 != 0 and k > (n+1)/2:
    res = 2*(k-(n+1)/2)
elif n % 2 == 0 and k <= n/2:
    res = 2*k-1
elif n % 2 == 0 and k > n/2:
    res = 2*(k-n/2)

print(int(res))
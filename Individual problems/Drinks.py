n = int(input())

drinks = [int(i) for i in input().split()]

print(sum(drinks)*100/(100*n))
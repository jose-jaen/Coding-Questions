n = int(input())
     
welfare = [int(i) for i in input().split()]
     
share = [max(welfare) - i for i in welfare]
     
print(sum(share))

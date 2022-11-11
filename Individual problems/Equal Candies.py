t = int(input())
     
for i in range(t):
    n = int(input())
    box = [int(j) for j in input().split()]
    print(sum([k-min(box) for k in box]))
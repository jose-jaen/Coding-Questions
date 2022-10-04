n = int(input())
     
x = [int(j) for j in input().split()]
     
maxi = x.index(max(x))
     
mini = [i for i in range(len(x)) if x[i] == min(x)]
     
res = maxi + len(x) - max(mini) - 1
     
print(res) if max(mini) > maxi else print(res - 1)
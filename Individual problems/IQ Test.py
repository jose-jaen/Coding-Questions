

n = int(input())
     
vec = [int(i) for i in input().split()]
     
even, odd = [], []
for i in range(3):
    even.append(vec[i]) if vec[i] % 2 == 0 else odd.append(vec[i])
     
if len(even) >= len(odd):
    res = [i for i in vec if i % 2 != 0]
    print(vec.index(res[0]) + 1)
else:
    res = [i for i in vec if i % 2 == 0]
    print(vec.index(res[0]) + 1)


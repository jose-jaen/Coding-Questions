t = int(input())
     
for i in range(t):
    distances = [int(j) for j in input().split()]
    print(sum([i - distances[0] > 0 for i in distances[1:]]))
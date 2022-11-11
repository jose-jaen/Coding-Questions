n = int(input())
     
vec = [int(i) for i in input().split()]
     
bonus = 0 if len(vec) % 2 == 0 else 1
     
p1, p2 = 0, 0
     
while p1 + p2 != sum(vec) and len(vec) > 1:
    scores = [vec[0], vec[len(vec)-1]]
    p1 += max(scores)
    vec.remove(max(scores))
    scores = [vec[0], vec[len(vec)-1]]
    p2 += max(scores)
    vec.remove(max(scores))
        
print(p1, p2) if bonus == 0 else print(p1+vec[0], p2)
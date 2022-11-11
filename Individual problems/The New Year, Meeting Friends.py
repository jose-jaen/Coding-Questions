x = sorted([int(i) for i in input().split()])
     
d = [x[1] - x[0], x[2] - x[1]]
ids = 2 if d.index(max(d)) == 1 else 0
     
print(min(d) + x[ids] - x[1]) if ids != 0 else print(min(d) + x[1] - x[ids])
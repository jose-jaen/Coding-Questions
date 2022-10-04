n = int(input())
     
t = [int(i) for i in input().split()]
     
skills = [t.count(j) for j in sorted(set(t))]
     
w = min(skills)
     
salir = False
     
print(0) if len(set(t)) != 3 else print(w)
     
if len(set(t)) == 3:
    for i in range(w):
        ids = [t.index(i) for i in sorted(set(t)) if i != 0]
        res = [str(i+1) for i in ids]
        print(' '.join(res))
        t = [t[i] if i not in ids else 0 for i in range(len(t))]
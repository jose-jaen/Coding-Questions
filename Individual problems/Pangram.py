n = int(input())
     
word = input()
lower = set([i for i in word if i.islower()])
upper = set([j.lower() for j in word if j.isupper()])
     
unique = [s for s in lower if s not in upper]
     
print('YES') if len(unique) + len(upper) == 26 else print('NO')

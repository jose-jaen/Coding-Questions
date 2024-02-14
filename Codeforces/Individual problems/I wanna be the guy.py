n = int(input())
     
p = [int(i) for i in input().split() if i != '0']
q = [int(j) for j in input().split() if j != '0']
     
levels_p = [int(s) for s in set(p[1:len(p)])]
levels_q = [int(k) for k in set(q[1:len(q)])]
     
levels_p.extend(levels_q)
     
print('I become the guy.') if n == len(set(levels_p)) else print('Oh, my keyboard!')

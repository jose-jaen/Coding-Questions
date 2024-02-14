n, m = [int(j) for j in input().split()]
         
vec = ''.join(['#'*m])
izq = ''.join(['#' + '.'*(m-1)])
dch = ''.join(['.'*(m-1) + '#'])
         
cont = 1
for i in range(n):
    if i % 2 == 0:
        print(vec)
    else:
        print(dch) if cont % 2 != 0 else print(izq)
        cont += 1
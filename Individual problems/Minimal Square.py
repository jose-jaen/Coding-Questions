t = int(input())

for i in range(t):
    a, b = [int(j) for j in input().split()]
    a_sol, b_sol = 2*a, 2*b
    print(min(a_sol, b_sol)**2) if min(a_sol, b_sol) > max(a, b) else print(max(a, b)**2)
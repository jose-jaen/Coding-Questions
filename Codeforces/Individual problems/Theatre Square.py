n, m, a = [int(j) for j in input().split()]
     
l1 = n/a if n%a == 0 else n//a + 1
l2 = m/a if m%a == 0 else m//a + 1
     
print(int(l1*l2))
n = int(input())
     
x = 9 if n % 2 != 0 else 8
y = n - 9 if n % 2 != 0 else n - 8
     
print(x, y)
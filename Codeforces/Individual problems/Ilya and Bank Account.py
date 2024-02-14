n = input()
     
a = n[0:len(n)-1]
b = n[0:len(n)-2]+n[len(n)-1]
     
print(max(int(n), int(a), int(b)))
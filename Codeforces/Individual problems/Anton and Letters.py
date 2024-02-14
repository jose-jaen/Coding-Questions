x = input()
     
x = x.replace('{', '')
x = x.replace('}', '')
     
y = [i for i in set(x) if i != ' ' and i != ',']
     
print(len(y))

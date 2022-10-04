

x = input()
     
if x[0].islower() and x[1:len(x)].isupper():
    x = x[0].upper()+x[1:len(x)].lower()
elif x.isupper():
    x = x.lower()
elif len(x) == 1 and x.islower():
    x = x.upper()
     
print(x)


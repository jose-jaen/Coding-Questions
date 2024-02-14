shift, phrase = input(), input()
     
a = [i for i in 'qwertyuiopasdfghjkl;zxcvbnm,./']
     
if shift == 'L':
    sol = [a[a.index(i)+1] for i in phrase]
else:
    sol = [a[a.index(i)-1] for i in phrase]
     
print(''.join(sol))
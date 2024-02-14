x, j = input(), input()
     
ber, bir = x, j
trans = []
i = len(ber) - 1
     
while i >= 0: 
    trans.append(ber[i])
    i -= 1
     
print('YES') if ''.join(trans) == bir else print('NO')
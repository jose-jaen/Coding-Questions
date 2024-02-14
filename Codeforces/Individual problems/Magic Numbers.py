number = input()
if any([True if str(i) in set(number) and i not in [1, 4] else False for i in range(10)]):
    print('NO')
elif number[0] != '1':
    print('NO')
elif '444' in number:
    print('NO')
else:
    print('YES')

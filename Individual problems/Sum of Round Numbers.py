t = int(input())
for i in range(t):
    res = []
    number = input()
    for j in range(len(number)):
        if j != len(number) - 1 and number[j] != '0':
            res.append(str(eval(number[j])*10**len(number[j + 1:])))
        elif j == len(number) - 1 and number[j] != '0':
            res.append(number[j])
    print(len(res))
    print(' '.join(res))
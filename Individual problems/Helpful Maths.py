x = input()

numbers = [int(i) for i in x if i != '+']

numbers.sort()

y = [str(j) for j in numbers]

s = '+'.join(y)

print(x) if len(numbers) == 1 else print(s)
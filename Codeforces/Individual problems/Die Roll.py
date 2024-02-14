from fractions import Fraction

maximo = max([int(i) for i in input().split()])
res = Fraction(6-maximo+1, 6)
print('1/1') if res == 1 else print(str(res))
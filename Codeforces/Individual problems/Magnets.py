magnets = [input() for i in range(int(input()))]
     
print(1 + sum(a != b for a, b in zip(magnets, magnets[1:])))
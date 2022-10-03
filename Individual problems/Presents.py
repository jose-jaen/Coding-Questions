n = int(input())

x = [int(i) for i in input().split()]

def argsort(seq):
    return sorted(range(n), key = seq.__getitem__)
    
y = [i+1 for i in argsort(x)]

print(y)
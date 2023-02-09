n, m = [int(i) for i in input().split()]

colors = ['C', 'M', 'Y']

count = 0
for i in range(n):
    movie = [s for s in input().split()]
    if len(set(colors) & set(movie)) > 0:
        count = 1

print('#Color') if count != 0 else print('#Black&White')
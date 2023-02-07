import string

w = input()
a = abs(string.ascii_lowercase.index(w[0]))
b = 26 - string.ascii_lowercase.index(w[0])
count = min(a, b)

for i in range(1, len(w)):
    a, b = string.ascii_lowercase.index(w[i - 1]), string.ascii_lowercase.index(w[i])
    c = abs(a - b)
    d = 26 - max(a, b) + min(a, b)
    count += min(c, d)

print(count)

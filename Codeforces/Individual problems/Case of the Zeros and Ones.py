import re

n = int(input())
string = ''.join(sorted(input()))
res = len(string)
if '1' in string:
    start_one = string.index('1')
    minimum_count = min(len(string[:start_one]), len(string[start_one:]))
    res = n - minimum_count*2
print(res)

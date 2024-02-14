from collections import Counter

grams = []
n = input()
word = input()
for i in range(len(word) - 1):
    grams.append(''.join(word[i:i+2]))

print(Counter(grams).most_common(1)[0][0])

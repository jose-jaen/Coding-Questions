from math import ceil

word = input()

cont = 0
for i in word:
    if i.islower():
        cont += 1

print(word.upper()) if ceil(len(word)/2) > cont else print(word.lower())
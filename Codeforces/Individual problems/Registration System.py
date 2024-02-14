t = int(input())
     
database = {}
for i in range(t):
    name = input()
    print(name + str(database[name]) if database.setdefault(name, 0) else 'OK')
    database[name] += 1
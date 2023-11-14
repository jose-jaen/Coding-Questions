t = int(input())
for _ in range(t):
    division = '1'
    rating = int(input())
    if rating <= 1399:
        division = '4'
    elif 1600 <= rating <= 1899:
        division = '2'
    elif 1400 <= rating <= 1599:
        division = '3'
    print(f'Division {division}')

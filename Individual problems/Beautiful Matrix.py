c1, c2 = 2, 2

row1 = [int(i) for i in input().split()]
row2 = [int(i) for i in input().split()]
row3 = [int(i) for i in input().split()]
row4 = [int(i) for i in input().split()]
row5 = [int(i) for i in input().split()]

if sum(row1) != 0:
    a, b = 0, [i for i in range(len(row1)) if row1[i] != 0][0]
elif sum(row2) != 0:
    a, b = 1, [i for i in range(len(row2)) if row2[i] != 0][0]
elif sum(row3) != 0:
    a, b = 2, [i for i in range(len(row3)) if row3[i] != 0][0]
elif sum(row4) != 0:
    a, b = 3, [i for i in range(len(row4)) if row4[i] != 0][0]
elif sum(row5) != 0:
    a, b = 4, [i for i in range(len(row5)) if row5[i] != 0][0]

r1, r2 = abs(c1-a), abs(c2-int(b))
print(r1+r2)
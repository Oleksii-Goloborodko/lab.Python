from random import random

M = 10
N = 5
a = []
for i in range(N):
    b = []
    for j in range(M):
        b.append(round(random() * 2))
    a.append(b)
    print(b)

c1 = int(input("Один столбец: ")) - 1
c2 = int(input("Другой столбец: ")) - 1

for i in range(N):
    a[i][c1], a[i][c2] = a[i][c2], a[i][c1]
    print(a[i])

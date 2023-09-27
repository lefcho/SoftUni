strings = input().split("|")

matrix = []

while strings:
    row = strings.pop().split()
    if row:
        matrix.append(row)

for row in matrix:
    print(*row, end=' ')
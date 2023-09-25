rows, columns = [int(x) for x in input().split()]

matrix = []
row = None

for i in range(rows):
    row = []
    for j in range(columns):
        row.append(chr(i + 97) + chr(j + i + 97) + chr(i + 97))
    matrix.append(row)

for r in matrix:
    print(*r)
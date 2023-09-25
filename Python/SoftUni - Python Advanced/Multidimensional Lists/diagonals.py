size = int(input())

matrix = []
prim_diagonal = []
sec_diagonal = []

for i in range(size):
    matrix.append([int(x) for x in input().split(", ")])

for i in range(len(matrix)):
    prim_diagonal.append(matrix[i][i])
    sec_diagonal.append(matrix[i][size - i - 1])

print("Primary diagonal: ", end='')
print(*prim_diagonal, sep=", ", end='. Sum: ')
print(sum(prim_diagonal))

print("Secondary diagonal: ", end='')
print(*sec_diagonal, sep=", ", end='. Sum: ')
print(sum(sec_diagonal))

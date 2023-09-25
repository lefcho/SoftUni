rows, columns = [int(x) for x in input().split()]

matrix = []
matches = 0

for i in range(rows):
    matrix.append(input().split())

for row in range(rows - 1):
    for col in range(columns - 1):
        if matrix[row][col] == matrix[row][col + 1] == matrix[row + 1][col] == matrix[row + 1][col + 1]:
            matches += 1

print(matches)
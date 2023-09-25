rows, columns = [int(x) for x in input().split()]

matrix = []
max_sum = float('-inf')
biggest_matrix = []

for i in range(rows):
    matrix.append([int(x) for x in input().split()])

for row in range(rows - 2):
    for col in range(columns - 2):
        row_1 = []
        row_2 = []
        row_3 = []
        for i in range(3):
            row_1.append(matrix[row][col + i])
            row_2.append(matrix[row + 1][col + i])
            row_3.append(matrix[row + 2][col + i])
        rows_sum = sum(row_1) + sum(row_2) + sum(row_3)
        if rows_sum > max_sum:
            max_sum = rows_sum
            biggest_matrix = []
            biggest_matrix.append(row_1)
            biggest_matrix.append(row_2)
            biggest_matrix.append(row_3)

print(f"Sum = {max_sum}")
for r in biggest_matrix:
    print(*r)
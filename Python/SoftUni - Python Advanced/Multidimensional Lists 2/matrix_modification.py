rows = int(input())

matrix = []

for i in range(rows):
    matrix.append([int(x) for x in input().split()])

command = input().split()

while command[0] != 'END':
    value = int(command.pop())
    col = int(command.pop())
    row = int(command.pop())
    operation = command.pop()

    if row >= len(matrix) or row < 0 or col >= len(matrix[row]) or col < 0:
        print('Invalid coordinates')
        command = input().split()
        continue

    if operation == 'Add':
        matrix[row][col] += value
    elif operation == "Subtract":
        matrix[row][col] -= value

    command = input().split()

for row in matrix:
    print(*row)
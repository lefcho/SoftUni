size = int(input())

matrix = []
ship_row = 0
ship_col = 0
catch = 0

for r in range(size):
    row = list(input())
    if 'S' in row:
        ship_row = r
        ship_col = row.index("S")
    matrix.append(row)

command = input()

while command != "collect the nets":
    matrix[ship_row][ship_col] = '-'
    if command == 'up':
        ship_row -= 1
        if ship_row < 0:
            ship_row = size - 1
    elif command == 'down':
        ship_row += 1
        if ship_row >= size:
            ship_row = 0
    elif command == 'right':
        ship_col += 1
        if ship_col >= size:
            ship_col = 0
    else:
        ship_col -= 1
        if ship_col < 0:
            ship_col = size - 1

    if matrix[ship_row][ship_col] == 'W':
        print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the ship: [{ship_row},{ship_col}]")
        exit(0)
    elif matrix[ship_row][ship_col].isnumeric():
        catch += int(matrix[ship_row][ship_col])

    matrix[ship_row][ship_col] = 'S'

    command = input()

if catch < 20:
    print(f"You didn't catch enough fish and didn't reach the quota! You need {20 - catch} tons of fish more.")
else:
    print("Success! You managed to reach the quota!")

if catch > 0:
    print(f"Amount of fish caught: {catch} tons.")

for row in matrix:
    print(*row, sep='')
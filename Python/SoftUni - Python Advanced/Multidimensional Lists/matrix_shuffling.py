from collections import deque

rows, columns = [int(x) for x in input().split()]
matrix = []

for _ in range(rows):
    matrix.append(input().split())

com = input()

while com != 'END':
    is_negative = False
    command = deque(com.split())
    swap = command.popleft()
    if swap != 'swap' or len(command) != 4:
        print("Invalid input!")
        com = input()
        continue
    command = [int(x) for x in command]

    for el in command:
        if el < 0:
            print("Invalid input!")
            com = input()
            is_negative = True
            continue

    if is_negative:
        print("Invalid input!")
        com = input()
        continue


    if command[0] >= rows or command[2] >= rows or command[1] >= columns or command[3] >= columns:
        print("Invalid input!")
        com = input()
        continue

    matrix[command[0]][command[1]], matrix[command[2]][command[3]] =\
        matrix[command[2]][command[3]], matrix[command[0]][command[1]]

    for r in matrix:
        print(*r)

    com = input()
from collections import deque

rows, columns = [int(x) for x in input().split()]
snake = input()
matrix = []
snake_index = 0

for i in range(rows):
    row = deque()
    for j in range(columns):
        if i % 2 == 0:
            row.append(snake[snake_index])
            snake_index += 1
            if snake_index >= len(snake):
                snake_index = 0
        else:
            row.appendleft(snake[snake_index])
            snake_index += 1
            if snake_index >= len(snake):
                snake_index = 0
    matrix.append(list(row))

for r in matrix:
    print("".join(r))
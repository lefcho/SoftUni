matrix = []
my_position = []
targets = 0

for row in range(5):
    matrix.append(input().split())
    for col in range(5):
        if matrix[row][col] == 'x':
            targets += 1
        elif matrix[row][col] == 'A':
            my_position = [row, col]

directions = {'left': (0, -1), 'right': (0, 1), 'up': (-1, 0), 'down': (1, 0)}
targets_down = []

n = int(input())

for _ in range(n):
    command  = input().split()
    if command[0] == 'shoot':
        r = my_position[0] + directions[command[1]][0]
        c = my_position[1] + directions[command[1]][1]
        while 0 <= r < 5 and 0 <= c < 5:
            if matrix[r][c] == 'x':
                matrix[r][c] = '.'
                targets -= 1
                targets_down.append([r, c])
                break
            r += directions[command[1]][0]
            c += directions[command[1]][1]
        if targets == 0:
            print(f"Training completed! All {len(targets_down)} targets hit.")
            break
    elif command[0] == 'move':
        steps = int(command[2])
        direction = command[1]
        if direction == 'up':
            r = my_position[0] - steps
            c = my_position[1]
        elif direction == 'down':
            r = my_position[0] + steps
            c = my_position[1]
        elif direction == 'left':
            r = my_position[0]
            c = my_position[1] - steps
        else:
            r = my_position[0]
            c = my_position[1] + steps

        if 0 <= r < 5 and 0 <= c < 5 and matrix[r][c] == '.':
            matrix[r][c] = 'A'
            matrix[my_position[0]][my_position[1]] = '.'
            my_position = [r, c]

if targets > 0:
    print(f'Training not completed! {targets} targets left.')
[print(row) for row in targets_down]

# field_size = 5
#
# field = []
# player_pos = [0, 0]
# targets = 0
# targets_hit = []
#
# for i in range(field_size):
#     row = input().split()
#     for el in row:
#         if el == 'x':
#             targets += 1
#         elif el == 'A':
#             player_pos[0] = i
#             player_pos[1] = row.index(el)
#     field.append(row)
#
# n = int(input())
#
# for _ in range(n):
#     command = input().split()
#     action = command[0]
#     direction = command[1]
#     if action == 'move':
#         steps = int(command[2])
#         if direction == "right":
#             next_step = player_pos[1] + steps
#             if not (0 <= next_step < field_size) or not field[player_pos[0]][next_step] == '.':
#                 pass
#             else:
#                 field[player_pos[0]][player_pos[1]] = '.'
#                 player_pos[1] = next_step
#                 field[player_pos[0]][player_pos[1]] = 'A'
#         elif direction == "left":
#             next_step = player_pos[1] - steps
#             if not (0 <= next_step < field_size) or not field[player_pos[0]][next_step] == '.':
#                 pass
#             else:
#                 field[player_pos[0]][player_pos[1]] = '.'
#                 player_pos[1] = next_step
#                 field[player_pos[0]][player_pos[1]] = 'A'
#         elif direction == "down":
#             next_step = player_pos[0] + steps
#             if not (0 <= next_step < field_size) or not field[next_step][player_pos[1]] == '.':
#                 pass
#             else:
#                 field[player_pos[0]][player_pos[1]] = '.'
#                 player_pos[0] = next_step
#                 field[player_pos[0]][player_pos[1]] = 'A'
#         elif direction == "up":
#             next_step = player_pos[0] - steps
#             if not (0 <= next_step < field_size) or not field[next_step][player_pos[1]] == '.':
#                 pass
#             else:
#                 field[player_pos[0]][player_pos[1]] = '.'
#                 player_pos[0] = next_step
#                 field[player_pos[0]][player_pos[1]] = 'A'
#     elif action == 'shoot':
#         if direction == 'right':
#             for shot in range(player_pos[1] + 1, field_size):
#                 if field[player_pos[0]][shot] == 'x':
#                     field[player_pos[0]][shot] = '.'
#                     targets -= 1
#                     targets_hit.append([player_pos[0], shot])
#                     break
#         elif direction == 'left':
#             for shot in range(player_pos[1] - 1, -1, -1):
#                 if field[player_pos[0]][shot] == 'x':
#                     field[player_pos[0]][shot] = '.'
#                     targets -= 1
#                     targets_hit.append([player_pos[0], shot])
#                     break
#         elif direction == 'down':
#             for shot in range(player_pos[0] + 1, field_size):
#                 if field[shot][player_pos[1]] == 'x':
#                     field[shot][player_pos[1]] = '.'
#                     targets -= 1
#                     targets_hit.append([shot, player_pos[1]])
#                     break
#         elif direction == 'up':
#             for shot in range(player_pos[0] - 1, -1, -1):
#                 if field[shot][player_pos[1]] == 'x':
#                     field[shot][player_pos[1]] = '.'
#                     targets -= 1
#                     targets_hit.append([shot, player_pos[1]])
#                     break
#         if targets <= 0:
#             print(f"Training completed! All {len(targets_hit)} targets hit.")
#
# if targets > 0:
#     print(f"Training not completed! {targets} targets left.")
#
# for tg in targets_hit:
#     print(tg)

n = int(input())

field = []
max_score = float('-inf')
bunny = (0, 0)
best_direction = ''
best_indexes = []

for r in range(n):
    row = []
    for i in input().split():
        if i == "X":
            row.append(i)
        elif i != 'B':
            row.append(int(i))
        else:
            row.append(i)
            bunny = (r, row.index(i))

    field.append(row)

bunny_r = bunny[0]
bunny_c = bunny[1]

current_ix = []
score = 0
# down
for i in range(bunny_r + 1, n):
    field_num = field[i][bunny_c]
    if field_num == 'X':
        break
    score += field_num
    current_ix.append([i, bunny_c])
if score > max_score and current_ix:
    max_score = score
    best_direction = 'down'
    best_indexes = current_ix.copy()

# up
current_ix = []
score = 0
for i in range(bunny_r - 1, -1, -1):
    field_num = field[i][bunny_c]
    if field_num == 'X':
        break
    score += field_num
    current_ix.append([i, bunny_c])
if score > max_score and current_ix:
    max_score = score
    best_direction = 'up'
    best_indexes = current_ix.copy()

# right
current_ix = []
score = 0
for i in range(bunny_c + 1, n):
    field_num = field[bunny_r][i]
    if field_num == 'X':
        break
    score += field_num
    current_ix.append([bunny_r, i])
if score > max_score and current_ix:
    max_score = score
    best_direction = 'right'
    best_indexes = current_ix.copy()

# left
current_ix = []
score = 0
for i in range(bunny_c - 1, -1, -1):
    field_num = field[bunny_r][i]
    if field_num == 'X':
        break
    score += field_num
    current_ix.append([bunny_r, i])
if score > max_score and current_ix:
    max_score = score
    best_direction = 'left'
    best_indexes = current_ix.copy()

print(best_direction)
for index in best_indexes:
    print(index)
print(max_score)
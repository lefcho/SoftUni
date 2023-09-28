presents = int(input())
size = int(input())
neighborhood = []

santa_pos = [0, 0]
nice_kids = 0
initial_nice_kids = 0

for row in range(size):
    neighborhood.append(input().split())
    for col in range(size):
        if neighborhood[row][col] == 'V':
            initial_nice_kids += 1
        elif neighborhood[row][col] == 'S':
            santa_pos = [row, col]

command = input()
while command != 'Christmas morning':
    if command == 'up':
        r = santa_pos[0] - 1
        c = santa_pos[1]
    elif command == 'down':
        r = santa_pos[0] + 1
        c = santa_pos[1]
    elif command == 'left':
        r = santa_pos[0]
        c = santa_pos[1] - 1
    else:
        r = santa_pos[0]
        c = santa_pos[1] + 1

    if 0 <= r < size and 0 <= c < size:
        if neighborhood[r][c] == 'V':
            presents -= 1
        elif neighborhood[r][c] == 'C':
            if neighborhood[r][c - 1] in 'XV':
                neighborhood[r][c - 1] = '-'
                presents -= 1
                if presents == 0:
                    neighborhood[santa_pos[0]][santa_pos[1]] = '-'
                    neighborhood[r][c] = "S"
                    break
            if neighborhood[r][c + 1] in 'XV':
                neighborhood[r][c + 1] = '-'
                presents -= 1
                if presents == 0:
                    neighborhood[santa_pos[0]][santa_pos[1]] = '-'
                    neighborhood[r][c] = "S"
                    break
            if neighborhood[r - 1][c] in 'XV':
                neighborhood[r - 1][c] = '-'
                presents -= 1
                if presents == 0:
                    neighborhood[santa_pos[0]][santa_pos[1]] = '-'
                    neighborhood[r][c] = "S"
                    break
            if neighborhood[r + 1][c] in 'XV':
                neighborhood[r + 1][c] = '-'
                presents -= 1
                if presents == 0:
                    neighborhood[santa_pos[0]][santa_pos[1]] = '-'
                    neighborhood[r][c] = "S"
                    break
        neighborhood[santa_pos[0]][santa_pos[1]] = '-'
        neighborhood[r][c] = "S"
        santa_pos[0] = r
        santa_pos[1] = c
        if presents == 0:
            break
    command = input()


for row in range(size):
    for col in range(size):
        if neighborhood[row][col] == 'V':
            nice_kids += 1

if nice_kids and not presents:
    print("Santa ran out of presents!")
for i in neighborhood:
    print(*i)

if not nice_kids:
    print(f"Good job, Santa! {initial_nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids} nice kid/s.")

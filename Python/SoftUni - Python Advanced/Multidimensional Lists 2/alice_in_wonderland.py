n = int(input())

field = []
alice_r = 0
alice_c = 0
tea = 0
# read
for r in range(n):
    row = input().split()
    for char in row:
        if char == "A":
            alice_r = r
            alice_c = row.index("A")
    field.append(row)

field[alice_r][alice_c] = "*"
while True:
    command = input()
    if command == 'left':
        alice_c -= 1
    elif command == 'right':
        alice_c += 1
    elif command == "down":
        alice_r += 1
    elif command == 'up':
        alice_r -= 1

    if not (0 <= alice_r < n) or not (0 <= alice_c < n):
        print("Alice didn't make it to the tea party.")
        break
    elif field[alice_r][alice_c] == "R":
        print("Alice didn't make it to the tea party.")
        field[alice_r][alice_c] = "*"
        break
    elif field[alice_r][alice_c] == ".":
        field[alice_r][alice_c] = "*"
    elif field[alice_r][alice_c].isdigit():
        tea += int(field[alice_r][alice_c])
        field[alice_r][alice_c] = "*"

    if tea >= 10:
        print("She did it! She went to the party.")
        break

for row in field:
    print(*row)
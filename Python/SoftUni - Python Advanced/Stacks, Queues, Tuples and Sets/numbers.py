from collections import deque

set_1 = set(int(x) for x in input().split())
set_2 = set(int(x) for x in input().split())

n = int(input())

for com in range(n):
    command = deque(input().split())

    if command[0] == 'Add':
        command.popleft()
        if command[0] == 'First':
            command.popleft()
            numbers = [int(x) for x in command]
            set_1.update(numbers)
        elif command[0] == 'Second':
            command.popleft()
            numbers = [int(x) for x in command]
            set_2.update(numbers)
    elif command[0] == 'Remove':
        command.popleft()
        if command[0] == 'First':
            command.popleft()
            numbers = [int(x) for x in command]
            set_1.difference_update(numbers)
        elif command[0] == 'Second':
            command.popleft()
            numbers = [int(x) for x in command]
            set_2.difference_update(numbers)

    elif command[0] == 'Check' and command[1] == 'Subset':
        print(set_1.issubset(set_2) or set_2.issubset(set_1))

print(*sorted(set_1), sep=", ")
print(*sorted(set_2), sep=", ")

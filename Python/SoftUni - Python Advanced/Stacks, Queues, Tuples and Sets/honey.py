from collections import deque

bees = deque(int(x) for x in input().split())
nectar_values = [int(x) for x in input().split()]
operations = deque(input().split())
honey_collected = 0

while bees and nectar_values:
    bee = bees[0]
    nectar = nectar_values.pop()

    if nectar < bee:
        continue

    symbol = operations.popleft()
    bees.popleft()

    if symbol == '+':
        honey_collected += abs(bee + nectar)
    elif symbol == '-':
        honey_collected += abs(bee - nectar)
    elif symbol == '*':
        honey_collected += abs(bee * nectar)
    elif nectar != 0 and symbol == '/':
        honey_collected += abs(bee / nectar)

print(f"Total honey made: {honey_collected}")

if bees:
    print("Bees left: ", end='')
    print(*bees, sep=', ')
if nectar_values:
    print("Nectar left: ", end='')
    print(*nectar_values, sep=", ")
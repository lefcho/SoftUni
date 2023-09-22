from collections import deque

chocolates = [int(x) for x in input().split(', ')]
cups_of_milk = deque(int(x) for x in input().split(', '))
milkshakes = 0
win = False

while chocolates and cups_of_milk:
    current_chocolate = chocolates[-1]
    current_milk = cups_of_milk[0]
    if current_chocolate <= 0 and current_milk <= 0:
        chocolates.pop()
        cups_of_milk.popleft()
        continue
    elif current_chocolate <= 0:
        chocolates.pop()
        continue
    elif current_milk <= 0:
        cups_of_milk.popleft()
        continue

    if current_chocolate == current_milk:
        milkshakes += 1
        cups_of_milk.popleft()
        chocolates.pop()
        if milkshakes >= 5:
            print("Great! You made all the chocolate milkshakes needed!")
            win = True
            break
        continue
    else:
        chocolates[-1] -= 5
        cups_of_milk.rotate(-1)

if not win:
    print("Not enough milkshakes.")
if chocolates:
    print(f"Chocolate: ", end='')
    print(*chocolates, sep=", ")
else:
    print("Chocolate: empty")
if cups_of_milk:
    print(f"Milk: ", end='')
    print(*cups_of_milk, sep=', ')
else:
    print("Milk: empty")
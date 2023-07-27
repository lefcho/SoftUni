events = input().split("|")
fail = False
energy = 100
coins = 100

for event in events:
    event_list = event.split("-")
    command = event_list[0]
    amount = int(event_list[1])

    if command == "rest":
        current_engy = energy
        energy += amount
        if energy > 100:
            energy = 100
        print(f"You gained {energy - current_engy} energy.")
        print(f"Current energy: {energy}.")
    elif command == "order":
        if energy >= 30:
            print(f"You earned {amount} coins.")
            coins += amount
            energy -= 30
        else:
            print("You had to rest!")
            energy += 50
    else:
        ingredient = command
        if coins >= amount:
            print(f"You bought {ingredient}.")
            coins -= amount
        else:
            print(f"Closed! Cannot afford {ingredient}.")
            fail = True
            break

if not fail:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")

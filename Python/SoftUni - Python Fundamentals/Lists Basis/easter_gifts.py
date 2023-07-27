gifts = input().split()

while True:
    command = input()
    if command == "No Money":
        for gift in gifts:
            if gift != "None":
                print(gift, end=" ")

        break

    elif command.startswith("OutOfStock "):
        command_list = command.split()
        gift = command_list[1]
        while gift in gifts:
            index = gifts.index(gift)
            gifts[index] = "None"

    elif command.startswith("Required "):
        command_list = command.split()
        gift = command_list[1]
        index = int(command_list[2])
        if 0 <= index < len(gifts):
            gifts[index] = gift

    elif command.startswith("JustInCase "):
        command_list = command.split()
        gift = command_list[1]
        gifts[-1] = gift

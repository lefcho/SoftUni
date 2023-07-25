dict_of_resources = {}
counter = 1

while True:
    command = input()
    if command == "stop":
        break
    elif counter % 2 != 0:
        current_resource = command
        if command not in dict_of_resources:
            dict_of_resources[command] = 0
    else:
        current_amount = int(command)
        dict_of_resources[current_resource] += current_amount

    counter += 1

for resource, amount in dict_of_resources.items():
    print(f"{resource} -> {amount}")
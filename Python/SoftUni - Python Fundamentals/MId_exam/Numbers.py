list_of_numbers = list(map(int, input().split()))

while True:
    command = input()
    if command == "Finish":
        break
    current_command = command.split()
    command = current_command[0]
    value = int(current_command[1])
    if command == "Add":
        list_of_numbers.append(value)
    elif command == "Remove":
        if value in list_of_numbers:
            list_of_numbers.remove(value)
    elif command == "Replace":
        if value in list_of_numbers:
            replace_index = list_of_numbers.index(value)
            list_of_numbers.remove(value)
            list_of_numbers.insert(replace_index, int(current_command[2]))
    elif command == "Collapse":
        counter = 0
        while counter < len(list_of_numbers):
            if list_of_numbers[counter] < value:
                del list_of_numbers[counter]
            else:
                counter += 1

for number in list_of_numbers:
    print(number, end=" ")


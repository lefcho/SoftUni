def change_string(initial_string, commands_list):
    char_to_change = commands_list[1]
    replacement = commands_list[2]
    changed_string = ''
    for char in initial_string:
        if char == char_to_change:
            changed_string += replacement
        else:
            changed_string += char
    return changed_string


def if_includes (initial_string, commands_list):
    substring = commands_list[1]
    if substring in initial_string:
        print("True")
    else:
        print("False")


def if_ends_with (initial_string, commands_list):
    substring = commands_list[1]
    if initial_string.endswith(substring):
        print("True")
    else:
        print("False")


def upper_string(initial_string):
    changed_string = initial_string.upper()
    return changed_string


def find_index(initial_string, commands_list):
    char_to_find = commands_list[1]
    index = 0
    if char_to_find in initial_string:
        for char in initial_string:
            if char == char_to_find:
                return index
            index += 1


def cut_string(initial_string, commands_list):
    start_index = int(commands_list[1])
    count = int(commands_list[2])
    changed_string = ''
    for index in range(start_index, start_index + count):
        changed_string += initial_string[index]
    return changed_string


string = input()
command = input()

while command != "Done":
    command_list = command.split()
    action = command_list[0]
    if action == "Change":
        string = change_string(string, command_list)
        print(string)
    elif action == "Includes":
        if_includes(string, command_list)
    elif action == "End":
        if_ends_with(string, command_list)
    elif action == "Uppercase":
        string = upper_string(string)
        print(string)
    elif action == "FindIndex":
        found_index = find_index(string, command_list)
        print(found_index)
    elif action == "Cut":
        string = cut_string(string, command_list)
        print(string)

    command = input()



string_list = input().split()

while True:
    command = input()
    list_to_add = []
    if command == "3:1":
        break
    command_list = command.split()
    if command_list[0] == "merge":
        start_index = int(command_list[1])
        end_index = int(command_list[2])
        if len(string_list) - 1 < end_index:
            end_index = len(string_list) - 1
        for i in range(start_index + 1, end_index + 1):
            string_list[start_index] += string_list.pop(start_index + 1)
    elif command_list[0] == "divide":
        divide_index = int(command_list[1])
        divide_times = int(command_list[2])
        divide_string = string_list.pop(divide_index)
        if len(divide_string) % divide_times == 0:
            divide_per = len(divide_string) // divide_times
            for i in range(0, len(divide_string), divide_per):
                list_to_add.append(divide_string[i:i + divide_per])
            for element in reversed(list_to_add):
                string_list.insert(divide_index, element)
        else:
            len_remainder = (len(divide_string) % divide_times) + 1
            last_part = divide_string[-len_remainder:]
            divide_per = len(divide_string) // divide_times
            divide_string = divide_string[:-len_remainder]
            for i in range(0, len(divide_string), divide_per):
                list_to_add.append(divide_string[i:i + divide_per])
            last_part += list_to_add.pop(-1)
            string_list.insert(divide_index, last_part)
            for element in reversed(list_to_add):
                string_list.insert(divide_index, element)

print(" ".join(string_list))

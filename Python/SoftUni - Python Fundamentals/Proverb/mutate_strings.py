second_string = input()
first_string = input()
final_string = ""

for i in range(1, len(first_string) + 1):
    first_part = first_string[:i]
    second_part = second_string[i:]
    final_string = first_part + second_part
    if i == 1:
        temp_string = final_string
        if second_string != temp_string:
            print(final_string)
    elif temp_string != final_string:
        print(final_string)

    temp_string = final_string

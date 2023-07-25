string = input()
final_string = ""
strength = 0

for i in range(len(string)):
    if strength > 0 and string[i] != ">":
        strength -= 1
    elif string[i] == ">":
        final_string += string[i]
        strength += int(string[i + 1])
    else:
        final_string += string[i]

print(final_string)
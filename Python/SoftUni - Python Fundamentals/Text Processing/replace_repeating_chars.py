initial = input()
fixed = ""
first_character = ""

for char in initial:
    if char != first_character:
        fixed += char
    first_character = char

print(fixed)
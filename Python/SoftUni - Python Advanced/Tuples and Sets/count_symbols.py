string = input()

char_dict = set()

for char in string:
    char_dict.add(char)

for char in sorted(char_dict):
    print(f"{char}: {string.count(char)} time/s")
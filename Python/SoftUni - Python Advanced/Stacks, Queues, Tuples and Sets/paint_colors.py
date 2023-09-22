from collections import deque


def check_string(string):

    if string == 'yellow':
        return string
    elif string == 'red':
        return string
    elif string == 'blue':
        return string
    elif string == 'orange':
        return string
    elif string == 'purple':
        return string
    elif string == 'green':
        return string
    else:
        return False


string = input().split(" ")
string = deque(string)
colors_list = []

while len(string) > 1:
    first_str = string.popleft()
    last_str = string.pop()
    substring = first_str + last_str
    answer = check_string(substring)
    if answer:
        colors_list.append(answer)
        continue
    else:
        middle = len(string) // 2
        if len(last_str) > 1:
            string.insert(middle, last_str[:-1])
        if len(first_str) > 1:
            string.insert(middle, first_str[:-1])

while string:
    substring = string.pop()
    answer = check_string(substring)
    if answer:
        colors_list.append(answer)
        continue
    elif len(substring) > 1:
        string.append(substring[:-1])

print(colors_list)
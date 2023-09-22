from collections import deque


def check_list(list_of_colors):
    if 'orange' in list_of_colors:
        if 'red' in list_of_colors and 'yellow' in list_of_colors:
            pass
        else:
            while 'orange' in list_of_colors:
                list_of_colors.remove('orange')
    if 'purple' in list_of_colors:
        if 'red' in list_of_colors and 'blue' in list_of_colors:
            pass
        else:
            while 'purple' in list_of_colors:
                list_of_colors.remove('purple')
    if 'green' in list_of_colors:
        if 'blue' in list_of_colors and 'yellow' in list_of_colors:
            pass
        else:
            while 'green' in list_of_colors:
                list_of_colors.remove('green')


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
    substring_1 = first_str + last_str
    substring_2 = last_str + first_str
    answer = check_string(substring_1)
    if not answer:
        answer = check_string(substring_2)
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

check_list(colors_list)
print(colors_list)
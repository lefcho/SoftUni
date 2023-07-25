import re

line = input()
while line:
    list_of_nums = re.findall("\d+", line)
    if list_of_nums:
        print(" ".join(list_of_nums), end=" ")
    line = input()

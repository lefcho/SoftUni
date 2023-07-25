import sys

f_list_of_numbers = input().split()
remove_count = int(input())
list_of_numbers = []

for number in f_list_of_numbers:
    list_of_numbers.append(int(number))
del f_list_of_numbers

for i in range(remove_count):
    smallest = sys.maxsize
    for num in list_of_numbers:
        if num < smallest:
            smallest = num

    list_of_numbers.remove(smallest)

for i in range(len(list_of_numbers)):
    if i != len(list_of_numbers) - 1:
        print(list_of_numbers[i], end=", ")
    else:
        print(list_of_numbers[i])

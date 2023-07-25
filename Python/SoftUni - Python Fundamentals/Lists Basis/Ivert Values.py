numbers = input()

num_list = numbers.split(' ')
reverse_list = []

for element in num_list:
    number = int(element) * -1
    reverse_list.append(number)

print(reverse_list)
factor = int(input())
count = int(input())
number_list = []

for i in range(1, count + 1):
    number = factor * i
    number_list.append(number)

print(number_list)
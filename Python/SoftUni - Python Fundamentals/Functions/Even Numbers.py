number_list = input().split()
num_list = []

for i in number_list:
    num_list.append(int(i))

is_even = lambda x: x % 2 == 0
evens = list(filter(is_even, num_list))

print(evens)

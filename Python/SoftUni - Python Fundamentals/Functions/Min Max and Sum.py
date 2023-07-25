number_list = input().split()

num_list = []

for i in number_list:
    num_list.append(int(i))

min_num = min(num_list)
max_num = max(num_list)
sum_nums = sum(num_list)

print(f"The minimum number is {min_num}")
print(f"The maximum number is {max_num}")
print(f"The sum number is: {sum_nums}")
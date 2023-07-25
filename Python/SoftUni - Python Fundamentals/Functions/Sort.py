number_list = input().split()

num_list = []
sorted_list = []

for i in number_list:
    num_list.append(int(i))

sorted_list = sorted(num_list)

print(sorted_list)

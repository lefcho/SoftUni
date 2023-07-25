list_of_numbers = list(map(int, input().split(", ")))
counter = 10
current_list = []
while True:
    current_list.clear()
    for i in range(len(list_of_numbers) - 1, -1, -1):
        if list_of_numbers[i] <= counter:
            current_list.append(list_of_numbers[i])
            list_of_numbers.remove(list_of_numbers[i])
    current_list.reverse()
    print(f"Group of {counter}'s: {current_list}")
    counter += 10
    if not list_of_numbers:
        break


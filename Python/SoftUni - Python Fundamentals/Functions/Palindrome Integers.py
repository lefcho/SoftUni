list_of_numbers = input().split(", ")

for number in list_of_numbers:
    left_to_right = []
    right_to_left = []
    for digit in number:
        left_to_right.append(digit)
    for digit in range(len(number) - 1, -1, -1):
        right_to_left.append(number[digit])

    if left_to_right == right_to_left:
        print(True)
    else:
        print(False)

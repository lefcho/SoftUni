list_of_items = list(map(int, input().split(", ")))
entry_point = int(input())
command = input()

left_side = list_of_items[0:entry_point:]
right_side = list_of_items[entry_point+1::]
entry_point_value = list_of_items[entry_point]
left_side_value = 0
right_side_value = 0

if command == "cheap":
    for item in left_side:
        if item < entry_point_value:
            left_side_value += item
    for item in right_side:
        if item < entry_point_value:
            right_side_value += item

if command == "expensive":
    for item in left_side:
        if item >= entry_point_value:
            left_side_value += item
    for item in right_side:
        if item >= entry_point_value:
            right_side_value += item

if left_side_value >= right_side_value:
    print(f"Left - {left_side_value}")
else:
    print(f"Right - {right_side_value}")


list_of_clothes = [int(x) for x in input().split()]
rack_value = int(input())
number_of_racks = 1
current_rack_value = 0

while list_of_clothes:
    clothing_value = list_of_clothes.pop()
    if clothing_value + current_rack_value > rack_value:
        number_of_racks += 1
        current_rack_value = clothing_value
    elif clothing_value + current_rack_value == rack_value:
        if list_of_clothes:
            number_of_racks += 1
        current_rack_value = 0
    else:
        current_rack_value += clothing_value

print(number_of_racks)
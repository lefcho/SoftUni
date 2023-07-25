from math import ceil

fake_numbers = input().split(", ")
numbers = []
beggars = int(input())
beggars_list = []

for number in fake_numbers:
    numbers.append(int(number))
del fake_numbers

for i in range(beggars):
    beggars_list.append(0)

rotations = ceil(len(numbers) / beggars)

for rotation in range(rotations):
    for beggar in range(len(beggars_list)):
        beggars_list[beggar] += numbers.pop(0)
        if len(numbers) == 0:
            del numbers
            break

print(beggars_list)

from collections import deque

materials = [int(x) for x in input().split()]
magic_values = deque(int(x) for x in input().split())
dolls = 0
wooden_trains = 0
teddy_bears = 0
bicycles = 0

while materials and magic_values:
    material = materials[-1]
    magic = magic_values[0]

    if material == 0 or magic == 0:
        if magic == 0:
            magic_values.popleft()
        if material == 0:
            materials.pop()
        continue

    level_of_magic = material * magic

    if level_of_magic < 0:
        materials[-1] = material + magic
        magic_values.popleft()
    elif level_of_magic == 150:
        magic_values.popleft()
        materials.pop()
        dolls += 1
    elif level_of_magic == 250:
        magic_values.popleft()
        materials.pop()
        wooden_trains += 1
    elif level_of_magic == 300:
        magic_values.popleft()
        materials.pop()
        teddy_bears += 1
    elif level_of_magic == 400:
        magic_values.popleft()
        materials.pop()
        bicycles += 1
    else:
        magic_values.popleft()
        materials[-1] += 15


if (dolls and wooden_trains) or (teddy_bears and bicycles):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print("Materials left: ", end='')
    materials.reverse()
    print(*materials, sep=', ')
if magic_values:
    print("Magic left: ", end='')
    print(*magic_values, sep=', ')
if bicycles:
    print(f'Bicycle: {bicycles}')
if dolls:
    print(f'Doll: {dolls}')
if teddy_bears:
    print(f'Teddy bear: {teddy_bears}')
if wooden_trains:
    print(f'Wooden train: {wooden_trains}')
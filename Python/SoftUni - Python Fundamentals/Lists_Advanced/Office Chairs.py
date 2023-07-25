number_of_rooms = int(input())
all_rooms = []
free_chairs = 0
number_of_room = 1
has_space = True

for i in range(number_of_rooms):
    all_rooms.append(input().split())

for room in all_rooms:
    chairs = len(room[0])
    people = int(room[1])
    if chairs >= people:
        free_chairs += chairs - people
    else:
        has_space = False
        needed_chairs = people - chairs
        print(f"{needed_chairs} more chairs needed in room {number_of_room}")
    number_of_room += 1

if has_space:
    print(f"Game On, {free_chairs} free chairs left")
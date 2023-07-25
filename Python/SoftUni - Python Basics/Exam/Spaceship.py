from math import floor

spaceship_width = float(input())
spaceship_length = float(input())
spaceship_height = float(input())
average_height = float(input())

v_spaceship = spaceship_height * spaceship_length * spaceship_width
v_room = 2 * 2 * (average_height + 0.4)
capacity = floor(v_spaceship / v_room)

if capacity >= 3 and capacity <= 10:
    print(f"The spacecraft holds {capacity} astronauts.")
elif capacity < 3:
    print("The spacecraft is too small.")
elif capacity > 10:
    print("The spacecraft is too big.")

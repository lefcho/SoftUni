n = int(input())
dict_of_cars = {}

for i in range(n):
    input_commands = input().split()
    command = input_commands[0]
    name = input_commands[1]
    if command == 'register':
        licence_plate = input_commands[2]
        if name not in dict_of_cars:
            dict_of_cars[name] = licence_plate
            print(f"{name} registered {licence_plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {dict_of_cars[name]}")
    else:
        if name in dict_of_cars:
            print(f"{name} unregistered successfully")
            del dict_of_cars[name]
        else:
            print(f"ERROR: user {name} not found")

for username, plate in dict_of_cars.items():
    print(f"{username} => {plate}")

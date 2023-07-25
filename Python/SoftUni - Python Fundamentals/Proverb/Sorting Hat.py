is_spoken = False
while True:
    name = input()
    if name == "Voldemort":
        print("You must not speak of that name!")
        is_spoken = True
        break
    elif name == "Welcome!":
        break
    elif len(name) < 5:
        print(f"{name} goes to Gryffindor.")
    elif len(name) == 5:
        print(f"{name} goes to Slytherin.")
    elif len(name) == 6:
        print(f"{name} goes to Ravenclaw.")
    else:
        print(f"{name} goes to Hufflepuff.")

if not is_spoken:
    print("Welcome to Hogwarts.")

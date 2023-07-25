coffee = 0
while True:
    action = input()
    if action == "coding" or action == "movie" or action == "dog" or action == "cat":
        coffee += 1
    elif action == "CODING" or action == "MOVIE" or action == "DOG" or action == "CAT":
        coffee += 2
    elif action == "END":
        break

if coffee <= 5:
    print(coffee)
else:
    print("You need extra sleep")
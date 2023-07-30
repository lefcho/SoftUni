dict_of_guests = {}
command = input()
unliked_meals = []

while command != "Stop":
    like_dislike, guest, meal = command.split("-")
    if like_dislike == "Like":
        if guest not in dict_of_guests:
            dict_of_guests[guest] = []
            dict_of_guests[guest].append(meal)
        else:
            if meal in dict_of_guests[guest]:
                pass
            else:
                dict_of_guests[guest].append(meal)

    elif like_dislike == "Dislike":
        if guest not in dict_of_guests:
            print(f"{guest} is not at the party.")
        else:
            if meal not in dict_of_guests[guest]:
                print(f"{guest} doesn't have the {meal} in his/her collection.")
            else:
                print(f"{guest} doesn't like the {meal}.")
                dict_of_guests[guest].remove(meal)
                if meal not in unliked_meals:
                    unliked_meals.append(meal)

    command = input()

for guest, liked_meals in dict_of_guests.items():
    print(f"{guest}", end=': ')
    print(", ".join(liked_meals))

print(f"Unliked meals: {len(unliked_meals)}")


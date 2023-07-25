from math import floor

breed = input()
gender = input()
cat_life = 0
valid = True

if breed == "British Shorthair":
    if gender == "m":
        cat_life = 13
    elif gender == "f":
        cat_life = 14
elif breed == "Siamese":
    if gender == "m":
        cat_life = 15
    elif gender == "f":
        cat_life = 16
elif breed == "Persian":
    if gender == "m":
        cat_life = 14
    elif gender == "f":
        cat_life = 15
elif breed == "Ragdoll":
    if gender == "m":
        cat_life = 16
    elif gender == "f":
        cat_life = 17
elif breed == "American Shorthair":
    if gender == "m":
        cat_life = 12
    elif gender == "f":
        cat_life = 13
elif breed == "Siberian":
    if gender == "m":
        cat_life = 11
    elif gender == "f":
        cat_life = 12
else:
    print(f"{breed} is invalid cat!")
    valid = False

if valid:
    cat_life = (cat_life * 12) / 6
    print(f"{floor(cat_life)} cat months")

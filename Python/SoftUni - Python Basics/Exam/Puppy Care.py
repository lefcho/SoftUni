food = int(input()) * 1000

while True:
    daily_food = input()
    if daily_food == "Adopted":
        break
    else:
        daily_food = int(daily_food)
    food -= daily_food

if food >= 0:
    print(f"Food is enough! Leftovers: {food} grams.")
elif food < 0:
    print(f"Food is not enough. You need {abs(food)} grams more.")

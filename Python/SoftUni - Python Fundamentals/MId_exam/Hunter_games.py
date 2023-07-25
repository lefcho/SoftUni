day_of_the_adventure = int(input())
player_count = int(input())
total_energy = float(input())
water_per_day = float(input())
food_per_day = float(input())
total_water = water_per_day * player_count * day_of_the_adventure
total_food = food_per_day * player_count * day_of_the_adventure

for day in range(1, day_of_the_adventure + 1):
    energy_for_the_day = float(input())
    total_energy -= energy_for_the_day
    if total_energy <= 0:
        break
    if day % 2 == 0:
        total_energy = total_energy + (5 * total_energy) / 100
        total_water = total_water - (30 * total_water) / 100
    if day % 3 == 0:
        total_food = total_food - (total_food / player_count)
        total_energy = total_energy + (10 * total_energy) / 100

if total_energy <= 0:
    print(f"You will run out of energy. You will be left with {total_food:.2f} food and {total_water:.2f} water.")
else:
    print(f"You are ready for the quest. You will be left with - {total_energy:.2f} energy!")
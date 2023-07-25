locations_number = int(input())

for i in range(locations_number):
    expected_gold = float(input())
    dig_days = int(input())
    all_gold = 0
    for j in range(dig_days):
        gold = float(input())
        all_gold += gold
        average_gold = all_gold / dig_days
        if j == dig_days - 1:
            if average_gold >= expected_gold:
                print(f"Good job! Average gold per day: {average_gold:.2f}.")
            else:
                needed_gold = expected_gold - average_gold
                print(f"You need {needed_gold:.2f} gold.")
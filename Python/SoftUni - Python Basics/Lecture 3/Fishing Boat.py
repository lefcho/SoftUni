budget = int(input())
season = input()
fisherman = int(input())
ship_cost = 0
cost = 0
discount = 0
extra_discount = 0
is_extra_discount_valid = True

if season == 'Spring':
    ship_cost = 3000
elif season == 'Summer' or season == 'Autumn':
    ship_cost = 4200
elif season == 'Winter':
    ship_cost = 2600

if fisherman <= 6:
    discount = ship_cost * 0.1
elif 7 < fisherman <= 11:
    discount = ship_cost * 0.15
elif fisherman >= 12:
    discount = ship_cost * 0.25

if fisherman % 2 == 1 or season == 'Autumn':
    is_extra_discount_valid = False

if is_extra_discount_valid:
    extra_discount = ship_cost * 0.05
    cost = ship_cost - discount - extra_discount
else:
    cost = ship_cost - discount - extra_discount

diff = abs(budget - cost)
if budget > cost:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")


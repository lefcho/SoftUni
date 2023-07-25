quantity = int(input())
days_till_xmas = int(input())

points = 0
money_spent = 0
ornament_price = 2
ornament_points = 5
skirt_price = 5
skirt_points = 3
garland_price = 3
garland_points = 10
lights_price = 15
lights_points = 17

for day in range(1, days_till_xmas + 1):
    if day % 11 == 0:
        quantity += 2
    if day % 2 == 0:
        money_spent += quantity * ornament_price
        points += ornament_points
    if day % 3 == 0:
        money_spent += quantity * (skirt_price + garland_price)
        points += skirt_points + garland_points
    if day % 5 == 0:
        money_spent += quantity * lights_price
        points += lights_points
        if day % 3 == 0:
            points += 30
    if day % 10 == 0:
        points -= 20
        money_spent += skirt_price + garland_price + lights_price

if days_till_xmas % 10 == 0:
    points -= 30

print(f"Total cost: {money_spent}")
print(f"Total spirit: {points}")

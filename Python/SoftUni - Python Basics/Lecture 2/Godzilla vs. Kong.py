budget = float(input())
extras = int(input())
outfit_price = float(input())

decor = budget * 0.1
outfit_cost = extras * outfit_price

if extras > 150:
    outfit_cost = outfit_cost - outfit_cost * 0.1

cost = outfit_cost + decor

if budget < cost:
    print("Not enough money!")
    needed = cost - budget
    fneeded = format(needed, '.2f')
    print(f"Wingard needs {fneeded} leva more.")
elif cost < budget:
    print("Action!")
    rest = budget - cost
    frest = format(rest, ".2f")
    print(f"Wingard starts filming with {frest} leva left.")


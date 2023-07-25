while True:
    country = input()
    if country == "End":
        break
    goal = float(input())
    current = 0

    while current < goal:
        money = float(input())
        current += money

    print(f"Going to {country}!")
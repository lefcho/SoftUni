def calculate_loaves(budget, price_per_kg_flour):
    price_per_pack_eggs = 0.75 * price_per_kg_flour
    price_per_liter_milk = 1.25 * price_per_kg_flour

    loaves_made = 0
    colored_eggs = 0

    while budget >= price_per_kg_flour + price_per_pack_eggs + (0.25 * price_per_liter_milk):
        budget -= (price_per_kg_flour + price_per_pack_eggs + (0.25 * price_per_liter_milk))
        loaves_made += 1
        colored_eggs += 3

        if loaves_made % 3 == 0:
            colored_eggs -= (loaves_made - 2)

    money_left = budget
    return loaves_made, colored_eggs, money_left

budget = float(input())
price_per_kg_flour = float(input())

loaves, eggs, money_left = calculate_loaves(budget, price_per_kg_flour)

print(f"You made {loaves} loaves of Easter bread! Now you have {eggs} eggs and {money_left:.2f}BGN left.")

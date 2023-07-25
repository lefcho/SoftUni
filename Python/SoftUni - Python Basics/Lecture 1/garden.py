area = floa(input())
garden_price = area * 7.61
discount = garden_price * 0.18
discount_gp = garden_price - discount

print(f"The final price is: {discount_gp} lv.")
print(f"The discount is: {discount} lv.")
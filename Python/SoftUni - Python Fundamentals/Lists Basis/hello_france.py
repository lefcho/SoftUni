items_to_buy = input().split("|")
budget = float(input())
sold_items_price = []
profit = 0
ticket = 150


for item in items_to_buy:
    item_list = item.split("->")
    item_name = item_list[0]
    item_price = float(item_list[1])
    if item_name == 'Clothes' and item_price <= 50:
        if item_price <= budget:
            budget -= item_price
            sold_items_price.append(item_price * 1.4)
            profit += 0.4 * item_price
    elif item_name == 'Shoes' and item_price <= 35:
        if item_price <= budget:
            budget -= item_price
            sold_items_price.append(item_price * 1.4)
            profit += 0.4 * item_price
    elif item_name == 'Accessories' and item_price <= 20.5:
        if item_price <= budget:
            budget -= item_price
            sold_items_price.append(item_price * 1.4)
            profit += 0.4 * item_price


for item in sold_items_price:
    print(f"{item:.2f}", end=" ")
print("")
print(f"Profit: {profit:.2f}")
if sum(sold_items_price) + budget >= ticket:
    print("Hello, France!")
else:
    print("Not enough money.")


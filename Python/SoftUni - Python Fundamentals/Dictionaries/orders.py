dict_of_items = {}

while True:
    command = input()
    if command == 'buy':
        break
    item_list = command.split()
    item_name = item_list[0]
    item_price = float(item_list[1])
    item_qty = int(item_list[2])

    if item_name not in dict_of_items:
        dict_of_items[item_name] = {}
        dict_of_items[item_name]["price"] = item_price
        dict_of_items[item_name]["quantity"] = item_qty
    else:
        dict_of_items[item_name]["price"] = item_price
        dict_of_items[item_name]["quantity"] += item_qty

for item, qualities in dict_of_items.items():
    total_price = qualities["price"] * qualities["quantity"]
    print(f"{item} -> {total_price:.2f}")
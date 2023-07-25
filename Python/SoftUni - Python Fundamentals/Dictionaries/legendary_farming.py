inventory_dict = {}

inventory_dict["shards"] = 0
inventory_dict["fragments"] = 0
inventory_dict["motes"] = 0
flag = False

while True:
    item_name = "None"
    obtained_items = input().split()
    for i in range(len(obtained_items)):
        if i % 2 == 0:
            quantity = int(obtained_items[i])
        else:
            item_name = obtained_items[i].lower()
            if item_name not in inventory_dict and item_name != "None":
                inventory_dict[item_name] = quantity
            elif item_name in inventory_dict:
                inventory_dict[item_name] += quantity


                if inventory_dict["shards"] >= 250:
                    flag = True
                    inventory_dict["shards"] -= 250
                    print('Shadowmourne obtained!')
                    break
                if inventory_dict["fragments"] >= 250:
                    inventory_dict["fragments"] -= 250
                    flag = True
                    print('Valanyr obtained!')
                    break
                if inventory_dict["motes"] >= 250:
                    inventory_dict["motes"] -= 250
                    flag = True
                    print('Dragonwrath obtained!')
                    break
    if flag:
        break

print(f'shards: {inventory_dict.pop("shards")}')
print(f'fragments: {inventory_dict.pop("fragments")}')
print(f'motes: {inventory_dict.pop("motes")}')

for item, amount in inventory_dict.items():
    print(f"{item}: {amount}")

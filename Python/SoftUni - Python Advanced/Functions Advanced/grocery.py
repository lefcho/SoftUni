def grocery_store(**kwargs):
    string_receipt = ''
    receipt = dict(sorted(kwargs.items(), key= lambda kvp: (-kvp[1], -len(kvp[0]), kvp[0])))
    for key, val in receipt.items():
        string_receipt += f"{key}: {val}\n"
    return string_receipt

print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))

print(grocery_store(    
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))


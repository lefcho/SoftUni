import re

command = input()
pattern = r">>([A-Za-z]+)<<(\d+\.?\d+)!(\d+)"
total_price = 0
print("Bought furniture:")
while command != "Purchase":
    items = re.findall(pattern, command)
    if items:
        print(items[0][0])
        total_price += float(items[0][1]) * float(items[0][2])
    command = input()

print(f"Total money spend: {total_price:.2f}")


number = int(input())
total = 0

for i in range(number):
    capsule = float(input())

    days = int(input())

    caps_per_day = int(input())
    if days < 1 or days > 31:
        continue
    if caps_per_day < 1 or caps_per_day > 2000:
        continue
    if capsule < 0.01 or capsule > 100:
        continue
    order = caps_per_day * capsule * days
    print(f"The price for the coffee is: ${order:.2f}")
    total += order

print(f"Total: ${total:.2f}")

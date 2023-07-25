flower = input()
quantity = int(input())
budget = int(input())
cost = 0

if flower == 'Roses':
    cost = quantity * 5
    if quantity > 80:
        cost = cost - (cost * 0.1)
elif flower == 'Dahlias':
    cost = quantity * 3.8
    if quantity > 90:
        cost = cost - (cost * 0.15)
elif flower == 'Tulips':
    cost = quantity * 2.8
    if quantity > 80:
        cost = cost - (cost * 0.15)
elif flower == 'Narcissus':
    cost = quantity * 3
    if quantity < 120:
        cost = cost + (cost * 0.15)
elif flower == 'Gladiolus':
    cost = quantity * 2.5
    if quantity < 80:
        cost = cost + (cost * 0.2)

diff = abs(budget - cost)
if budget > cost:
    print(f"Hey, you have a great garden with {quantity} {flower} and {diff:.2f} leva left.")
else:
    print(f"Not enough money, you need {diff:.2f} leva more.")


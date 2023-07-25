days = int(input())
room = input()
grade = input()
nights = days - 1
price = 0

if room == 'room for one person':
    price = nights * 18
elif room == 'apartment':
    if days < 10:
        price = (nights * 25) * 0.7
    elif days <= 15:
        price = (nights * 25) * 0.65
    elif days > 15:
        price = (nights * 25) * 0.5
elif room == 'president apartment':
    if days < 10:
        price = (nights * 35) * 0.9
    elif days <= 15:
        price = (nights * 35) * 0.85
    elif days > 15:
        price = (nights * 35) * 0.8

if grade == 'positive':
    price = price + price * 0.25
elif grade == 'negative':
    price = price - price * 0.1

print(f'{price:.2f}')
page_price = float(input())
head_price = float(input())
discount_percent = int(input())
designer = float(input())
team_percent = int(input())

price = page_price * 899 + head_price * 2
price = price - (price * discount_percent / 100)
price += designer
price = price - (price * team_percent / 100)

print(f"Avtonom should pay {price:.2f} BGN.")
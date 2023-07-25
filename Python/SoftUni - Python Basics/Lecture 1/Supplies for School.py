pens = int(input()) * 5.8
markers = int(input()) * 7.2
liters = int(input()) * 1.2
discount = int(input())
total = pens + markers + liters
discount_price = total - (total * (discount / 100))
print(discount_price)


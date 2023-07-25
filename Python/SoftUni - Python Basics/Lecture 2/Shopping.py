budget = float(input())
graphics_cards = int(input())
processor = int(input())
ram_memory = int(input())

graphics_cards_price = 250 * graphics_cards
processor_price = processor * (graphics_cards_price * 0.35)
ram_memory_price = ram_memory * (graphics_cards_price * 0.1)

price_all = graphics_cards_price + processor_price + ram_memory_price

if graphics_cards > processor:
    price_all = price_all - (price_all * 0.15)

if budget >= price_all:
    rest = budget - price_all
    f_rest = format(rest, '.2f')
    print(f'You have {f_rest} leva left!')
elif budget < price_all:
    needed = price_all - budget
    f_needed = format(needed, '.2f')
    print(f'Not enough money! You need {f_needed} leva more!')


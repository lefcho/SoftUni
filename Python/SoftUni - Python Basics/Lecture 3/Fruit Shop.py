fruit = input()
day = input()
quantity = float(input())
is_valid = False

if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday':
    if fruit == 'banana':
        price = 2.5
        is_valid = True
    elif fruit == 'apple':
        price = 1.2
        is_valid = True
    elif fruit == 'orange':
        price = 0.85
        is_valid = True
    elif fruit == 'grapefruit':
        price = 1.45
        is_valid = True
    elif fruit == 'kiwi':
        price = 2.7
        is_valid = True
    elif fruit == 'pineapple':
        price = 5.5
        is_valid = True
    elif fruit == 'grapes':
        price = 3.85
        is_valid = True

if day == 'Saturday' or day == 'Sunday':
    if fruit == 'banana':
        price = 2.7
        is_valid = True
    elif fruit == 'apple':
        price = 1.25
        is_valid = True
    elif fruit == 'orange':
        price = 0.9
        is_valid = True
    elif fruit == 'grapefruit':
        price = 1.6
        is_valid = True
    elif fruit == 'kiwi':
        price = 3
        is_valid = True
    elif fruit == 'pineapple':
        price = 5.6
        is_valid = True
    elif fruit == 'grapes':
        price = 4.2
        is_valid = True

if is_valid:
    total = quantity * price
    print(f"{total:.2f}")
else:
    print('error')

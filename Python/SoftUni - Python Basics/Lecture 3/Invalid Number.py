number = int(input())
valid = False

if 100 <= number <= 200 or number == 0:
    valid = True

if not valid:
    print('invalid')


city = input()
sales = float(input())
is_valid = False
commissions = 0

if city == 'Sofia':
    if 0 <= sales <= 500:
        commissions = sales * 0.05
        is_valid = True
    elif 500 < sales <= 1000:
        commissions = sales * 0.07
        is_valid = True
    elif 1000 < sales <= 10000:
        commissions = sales * 0.08
        is_valid = True
    elif sales > 10000:
        commissions = sales * 0.12
        is_valid = True
elif city == 'Varna':
    if 0 <= sales <= 500:
        commissions = sales * 0.045
        is_valid = True
    elif 500 < sales <= 1000:
        commissions = sales * 0.075
        is_valid = True
    elif 1000 < sales <= 10000:
        commissions = sales * 0.1
        is_valid = True
    elif sales > 10000:
        commissions = sales * 0.13
        is_valid = True
elif city == 'Plovdiv':
    if 0 <= sales <= 500:
        commissions = sales * 0.055
        is_valid = True
    elif 500 < sales <= 1000:
        commissions = sales * 0.08
        is_valid = True
    elif 1000 < sales <= 10000:
        commissions = sales * 0.12
        is_valid = True
    elif sales > 10000:
        commissions = sales * 0.145
        is_valid = True

if is_valid:
    print(f"{commissions:.2f}")
else:
    print('error')
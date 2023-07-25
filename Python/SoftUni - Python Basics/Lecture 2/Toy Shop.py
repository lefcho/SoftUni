vacation = float(input())
puzzles = int(input())
dolls = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())

puzzles_income = puzzles * 2.6
dolls_income = dolls * 3
bears_income = bears * 4.1
minions_income = minions * 8.2
trucks_income = trucks * 2

income = puzzles_income + dolls_income + bears_income + minions_income + trucks_income
items_ordered = puzzles + dolls + bears + minions + trucks

if items_ordered >= 50:
    discount = income * 0.25
    income = income - discount

rent = income * 0.1
income = income - rent

if income >= vacation:
    rest = income - vacation
    f_rest = format(rest, '.2f')
    print(f"Yes! {f_rest} lv left.")
else:
    needed = vacation - income
    f_needed = format(needed, '.2f')
    print(f"Not enough money! {f_needed} lv needed.")
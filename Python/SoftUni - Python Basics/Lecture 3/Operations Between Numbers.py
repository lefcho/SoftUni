number_1 = int(input())
number_2 = int(input())
symbol = input()
result = 0
even_odd = ''

if symbol == '+':
    result = number_2 + number_1
elif symbol == '-':
    result = number_1 - number_2
elif symbol == '*':
    result = number_2 * number_1
elif symbol == '/':
    if number_2 == 0:
        print(f"Cannot divide {number_1} by zero")
    else:
        result = number_1 / number_2
elif symbol == '%':
    if number_2 == 0:
        print(f"Cannot divide {number_1} by zero")
    else:
        result = number_1 % number_2

if result % 2 == 0:
    even_odd = 'even'
else:
    even_odd = 'odd'

if symbol == '/' and number_2 != 0:
    print(f"{number_1} {symbol} {number_2} = {result:.2f}")
elif symbol == '%' and number_2 != 0:
    print(f"{number_1} {symbol} {number_2} = {result}")
elif symbol == '+' or symbol == '-' or symbol == '*':
    print(f"{number_1} {symbol} {number_2} = {result} - {even_odd}")
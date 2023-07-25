def sum_numbers(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def add_and_subtract(num1, num2, num3):
    n = sum_numbers(num1, num2)
    return subtract(n, num3)


n1 = int(input())
n2 = int(input())
n3 = int(input())

print(add_and_subtract(n1, n2, n3))

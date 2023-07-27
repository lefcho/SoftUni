def factorial_division(num1, num2):
    sum1 = 1
    sum2 = 1
    for i in range(2, num1 + 1):
        sum1 *= i
    for i in range(2, num2 + 1):
        sum2 *= i
    result = sum1 / sum2
    return result


n1 = int(input())
n2 = int(input())

result = factorial_division(n1, n2)

print(f'{result:.2f}')

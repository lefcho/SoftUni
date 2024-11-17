def recursive_factorial(number):
    if number == 0:
        return 1
    return number * recursive_factorial(number - 1)


n = int(input())

print(recursive_factorial(n))

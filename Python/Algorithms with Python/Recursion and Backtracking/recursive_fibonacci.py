def recursive_fib(number):
    if number <= 1:
        return 1
    return recursive_fib(number - 1) + recursive_fib(number - 2)


n = int(input())
print(recursive_fib(n))
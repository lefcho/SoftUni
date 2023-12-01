def fibonacci():
    current_n = 0
    next_n = 1
    while True:
        yield current_n
        current_n, next_n = next_n,current_n + next_n


generator = fibonacci()
for i in range(5):
    print(next(generator))
print()
generator = fibonacci()
for i in range(1):
    print(next(generator))

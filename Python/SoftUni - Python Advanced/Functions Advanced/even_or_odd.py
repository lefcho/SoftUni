def even_odd(*args):
    list_args = list(args)
    even_or_odd = list_args.pop()
    if even_or_odd == 'even':
        return list(filter(lambda x: x % 2 == 0, list_args))
    return list(filter(lambda x: x % 2 != 0, list_args))

print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))

def even_odd_filter(**kwargs):
    for key, val in kwargs.items():
        if key == 'odd':
            kwargs[key] = list(filter(lambda x: x % 2 != 0, val))
        else:
            kwargs[key] = list(filter(lambda x: x % 2 == 0, val))

    return dict(sorted(kwargs.items(), key= lambda x: len(x[1]), reverse=True))

print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))

print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))

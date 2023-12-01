def possible_permutations(start):
    if len(start) <= 1:
        yield start
    else:
        for i in range(len(start)):
            for perm in possible_permutations(start[:i] + start[i + 1:]):
                yield [start[i]] + perm


[print(n) for n in possible_permutations([1, 2, 3])]
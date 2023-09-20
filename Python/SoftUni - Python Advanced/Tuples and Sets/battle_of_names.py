rows = int(input())

odd_set = set()
even_set = set()

for row in range(1, rows + 1):
    sum_of_chars = 0
    name = input()
    for char in name:
        sum_of_chars += ord(char)

    sum_of_chars = sum_of_chars // row

    if sum_of_chars % 2 == 0:
        even_set.add(sum_of_chars)
    else:
        odd_set.add(sum_of_chars)

if sum(odd_set) > sum(even_set):
    diff = odd_set.difference(even_set)
    for_print = [str(x) for x in diff]
elif sum(even_set) > sum(odd_set):
    sym_diff = odd_set.symmetric_difference(even_set)
    for_print = [str(x) for x in sym_diff]
else:
    union = odd_set.union(even_set)
    for_print = [str(x) for x in union]

print(", ".join(for_print))
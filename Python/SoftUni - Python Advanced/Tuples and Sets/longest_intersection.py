n = int(input())

biggest_intersection = []

for _ in range(n):
    set_1 = set()
    set_2 = set()
    set_1_s, set_2_s = input().split('-')
    start_1, end_1 = [int(x) for x in set_1_s.split(',')]
    start_2, end_2 = [int(x) for x in set_2_s.split(',')]

    for num in range(start_1, end_1 + 1):
        set_1.add(num)

    for num in range(start_2, end_2 + 1):
        set_2.add(num)

    intersection = set_1.intersection(set_2)

    if _ == 0:
        biggest_intersection = intersection.copy()
    elif len(intersection) > len(biggest_intersection):
        biggest_intersection = intersection.copy()



print(f"Longest intersection is {list(biggest_intersection)} with length {len(biggest_intersection)}")
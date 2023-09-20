n = int(input())

elements = set()

for _ in range(n):
    el_list = input().split()
    for el in el_list:
        elements.add(el)

for element in elements:
    print(element)
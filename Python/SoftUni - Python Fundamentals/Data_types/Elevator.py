from math import ceil

people_in_elevator = int(input())
capacity = int(input())

courses = ceil(people_in_elevator / capacity)

print(courses)
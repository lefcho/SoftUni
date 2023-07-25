n = int(input())
dict_of_students = {}

for _ in range(n):
    student = input()
    grade = float(input())
    if student not in dict_of_students:
        dict_of_students[student] = grade
    else:
        dict_of_students[student] = (dict_of_students[student] + grade) / 2

keys_to_remove = []

for s in dict_of_students.keys():
    if dict_of_students[s] < 4.5:
        keys_to_remove.append(s)

for k in keys_to_remove:
    del dict_of_students[k]


for student, grade in dict_of_students.items():
    print(f"{student} -> {grade:.2f}")
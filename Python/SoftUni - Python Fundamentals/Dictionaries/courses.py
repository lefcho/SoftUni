dict_of_courses = {}

while True:
    command = input()
    if command == 'end':
        break

    command_list = command.split(" : ")
    course = command_list[0]
    student = command_list[1]
    if course not in dict_of_courses:
        dict_of_courses[course] = []
        dict_of_courses[course].append(student)
    else:
        dict_of_courses[course].append(student)

for current_course, lst_students in dict_of_courses.items():
    print(f"{current_course}: {len(lst_students)}")
    for name in lst_students:
        print(f"-- {name}")
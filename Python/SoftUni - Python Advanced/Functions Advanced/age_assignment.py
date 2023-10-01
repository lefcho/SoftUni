def age_assignment(*args, **kwargs):
    people = {}
    people_string = ''
    for name in args:
        people[name] = kwargs[name[0]]
    people = dict(sorted(people.items(), key= lambda kvp: kvp[0]))
    for name, age in people.items():
        people_string += f"{name} is {age} years old.\n"
    return people_string

print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))

name = input()
fails = 0
total = 0
s_class = 1
average = 0

while True:
    grade = float(input())
    if grade < 4:
        fails += 1
        if fails >= 2:
            print(f"{name} has been excluded at {s_class} grade")
            break
        continue
    s_class += 1
    total += grade
    if s_class > 12:
        print(f"{name} graduated. Average grade: {total / 12:.2f}")
        break

start = int(input())
end = int(input())
goal = int(input())
counter = 0
flag = False

for j in range(start, end + 1):
    for i in range(start, end + 1):
        current = j + i
        counter += 1
        if current == goal:
            print(f"Combination N:{counter} ({j} + {i} = {goal})")
            flag = True
            break
    if flag:
        break

if not flag:
    print(f"{counter} combinations - neither equals {goal}")
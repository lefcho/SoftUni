n = int(input())

for i in range(n):
    string = input()
    is_not_pure = False
    for j in range(len(string)):
        if string[j] == '.' or string[j] == ',' or string[j] == '_':
            is_not_pure = True
    if is_not_pure:
        print(f"{string} is not pure!")
    else:
        print(f"{string} is pure.")
while True:
    string = input()
    if string == 'End':
        break
    elif string == "SoftUni":
        continue
    else:
        for i in range(len(string)):
            print(f"{string[i]}{string[i]}", end="")
        print()
        
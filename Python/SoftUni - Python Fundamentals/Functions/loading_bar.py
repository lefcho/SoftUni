def print_loading_bar(percentage):
    if percentage == 100:
        print("100% Complete!")
        print("[%%%%%%%%%%]")
    else:
        print(f"{percentage}%", end=" ")
        print("[", end="")
        for i in range(percentage // 10):
            print("%", end="")
        for i in range(10 - (percentage // 10)):
            print(".", end="")
        print(']')
        print("Still loading...")



n = int(input())

print_loading_bar(n)

def perfect_check(number):
    current = 0
    for i in range(1, int(number / 2) + 1):
        if number % i == 0:
            current += i

    if number == current and number > 0:
        return True
    else:
        return False


num = int(input())

if perfect_check(num):
    print("We have a perfect number!")
else:
    print("It's not so perfect.")

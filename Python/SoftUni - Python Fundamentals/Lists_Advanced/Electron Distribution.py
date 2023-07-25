number_of_electrons = int(input())
list_of_shells = []
counter = 1

while True:
    current_shell = 2 * counter * counter
    temp_electrons = number_of_electrons
    number_of_electrons -= current_shell
    if number_of_electrons < 0:
        current_shell = temp_electrons
    list_of_shells.append(current_shell)
    if number_of_electrons < 1:
        break
    counter += 1

print(list_of_shells)
numbers_dictionary = {}

line = input('Enter integer as STRING or "Search": ')

while line != "Search":
    number_as_string = line
    try:
        number = int(input('Enter integer: '))
    except ValueError:
        print("The variable number must be an integer")
    else:
        numbers_dictionary[number_as_string] = number
    finally:
        line = input('Enter integer as STRING or "Search": ')

line = input('"Remove" or Search for: ')

while line != "Remove":
    searched = line
    try:
        print(numbers_dictionary[searched])
    except KeyError:
        print("Number does not exist in dictionary")
    finally:
        line = input('"Remove" or Search for: ')

line = input('"End" or Remove: ')

while line != "End":
    searched = line
    try:
        del numbers_dictionary[searched]
    except KeyError:
        print("Number does not exist in dictionary")
    finally:
        line = input('"End" or Remove: ')
print(numbers_dictionary)


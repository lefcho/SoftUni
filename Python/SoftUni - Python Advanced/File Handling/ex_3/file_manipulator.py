import os

command = input()

while command != 'End':
    command, file_name, *args = command.split('-')
    if command == 'Create':
        open(file_name, 'w').close()
    elif command == 'Add':
        with open(file_name, 'a') as file:
            file.write(f'{" ".join(args)}\n')
    elif command == 'Replace':
        try:
            with open(file_name) as file:
                file_content = file.read()
                new_content = file_content.replace(args[0], args[1])
        except FileNotFoundError:
            print("An error occurred")
        else:
            with open(file_name, 'w') as file:
                file.write(new_content)
    elif command == 'Delete':
        try:
            os.remove(file_name)
        except FileNotFoundError:
            print("An error occurred")

    command = input()

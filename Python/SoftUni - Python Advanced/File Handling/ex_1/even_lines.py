with open('text.txt') as text:
    for num_of_line, line in enumerate(text.readlines()):
        if num_of_line % 2 == 0:
            words = line.split()
            for _ in range(len(words)):
                for char in words.pop():
                    if char in ',.!?-':
                        char = '@'
                    print(char, end='')
                print(" ", end='')
            print()
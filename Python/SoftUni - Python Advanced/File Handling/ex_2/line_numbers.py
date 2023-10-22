with open('text.txt') as text, open('output.txt', 'w') as output:
    result = ''
    for num_of_line, line in enumerate(text.readlines()):
        num_of_letters = 0
        num_of_punct = 0
        for el in line:
            if el.isalpha():
                num_of_letters += 1
            elif el in ".,?!-'":
                num_of_punct += 1
        result += f'Line {num_of_line+1}: {line.rstrip()} ({num_of_letters}) ({num_of_punct})\n'

    output.write(result)
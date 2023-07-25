def print_ascii_in_range(start, end):
    for char in range(ord(start) + 1, ord(end)):
        print(chr(char), end=" ")


start = input()
end = input()

print_ascii_in_range(start, end)


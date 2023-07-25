# def palindrome_check(num):
#     if len(num) % 2 == 0:
#         middle = int(len(num) / 2)
#     else:
#         middle = int(len(num) / 2) + 1
#     first_half = []
#     second_half = []
#     is_palindrome = True
#     for i in range(middle):
#         first_half.append(num[i])
#     for i in range(len(num) - 1, middle - 1, -1):
#         second_half.append(num[i])
#
#     if first_half != second_half:
#         is_palindrome = False
#     return is_palindrome


num = input()
first_half = []
second_half = []
is_palindrome = True
if len(num) % 2 == 0:
    middle = int(len(num) / 2)
    for i in range(middle):
        first_half.append(num[i])
    for i in range(len(num) - 1, middle - 1, -1):
        second_half.append(num[i])
else:
    middle = int(len(num) / 2) + 1
    for i in range(middle):
        first_half.append(num[i])
    for i in range(len(num) - 1, middle, -1):
        second_half.append(num[i])
first_half = []
second_half = []
is_palindrome = True

if first_half != second_half:
    is_palindrome = False

print(is_palindrome)

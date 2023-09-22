deque_of_symbs = input().split()
num_to_operate = []
operator = ''

for symb in deque_of_symbs:
    result = 0
    if symb == '*':
        result = 1
        for num in num_to_operate:
            result *= num
        # print(*num_to_operate, sep=" * ", end='')
        num_to_operate.clear()
        num_to_operate.append(result)
#         print(f" = {result}")
    elif symb == '/':
        for index in range(len(num_to_operate) - 1):
            if index == 0:
                result = num_to_operate[0]
            result = result // num_to_operate[index + 1]
#         print(*num_to_operate, sep=" / ", end='')
        num_to_operate.clear()
        num_to_operate.append(result)
#         print(f" = {result}")
    elif symb == '+':

        for num in num_to_operate:
            result += num
#         print(*num_to_operate, sep=" + ", end="")
        num_to_operate.clear()
        num_to_operate.append(result)
#         print(f" = {result}")
    elif symb == '-':
        for index in range(len(num_to_operate) - 1):
            if index == 0:
                result = num_to_operate[0]
            result = result - num_to_operate[index + 1]
#         print(*num_to_operate, sep=" - ", end="")
        num_to_operate.clear()
        num_to_operate.append(result)
#         print(f" = {result}")
    else:
        num_to_operate.append(int(symb))

print(result)
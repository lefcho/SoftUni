number_count = int(input())

sum_1 = 0
sum_2 = 0

for i in range(number_count):
    number = int(input())
    if i % 2 == 0:
        sum_1 += number
    else:
        sum_2 += number

if sum_1 == sum_2:
    print('Yes')
    print(f'Sum = {sum_2}')
else:
    diff = abs(sum_2 - sum_1)
    print('No')
    print(f'Diff = {diff}')
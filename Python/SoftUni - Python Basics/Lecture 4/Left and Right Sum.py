number_count = int(input())

sum_1 = 0
sum_2 = 0

for i in range(number_count):
    number_1 = int(input())
    sum_1 += number_1
for j in range(number_count):
    number_2 = int(input())
    sum_2 += number_2

if sum_1 == sum_2:
    print(f'Yes, sum = {sum_2}')
else:
    diff = abs(sum_2 - sum_1)
    print(f'No, diff = {diff}')

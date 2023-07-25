needed_sum = int(input())
current_sum = 0

while needed_sum > current_sum:
    number = int(input())
    current_sum += number

print(current_sum)
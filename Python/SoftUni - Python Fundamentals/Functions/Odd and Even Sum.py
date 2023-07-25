def odd_and_even_sums(number):
    odd_sum = 0
    even_sum = 0
    for digit in number:
        if int(digit) % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)
    return odd_sum, even_sum


num = input()

odd_sum, even_sum = odd_and_even_sums(num)

print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")

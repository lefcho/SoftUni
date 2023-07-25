def smallest_of_three(num1, num2, num3):
    smallest = num1
    if num2 < num1:
        smallest = num2
    if num3 < num1 and num3 < num2:
        smallest = num3
    return smallest


n1 = int(input())
n2 = int(input())
n3 = int(input())

print(smallest_of_three(n1, n2, n3))

n = int(input())
result = 0

for i in range(n):
    current_char = input()
    result += ord(current_char)

print(f"The sum equals: {result}")
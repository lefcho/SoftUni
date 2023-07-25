projection_type = input()
rows = int(input())
colons = int(input())
total = 0

if projection_type == 'Premiere':
    total = rows * colons * 12.
elif projection_type == 'Normal':
    total = rows * colons * 7.5
elif projection_type == 'Discount':
    total = rows * colons * 5

print(f"{total:.2f} leva")

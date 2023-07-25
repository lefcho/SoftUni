n = int(input())
capacity = 255
current_capacity = 0

for i in range(n):
    current_liters = int(input())
    current_capacity += current_liters
    if current_capacity > capacity:
        print("Insufficient capacity!")
        current_capacity -= current_liters

print(current_capacity)
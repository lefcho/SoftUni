n = int(input())
m = int(input())
s = int(input())

for i in range(m, n - 1, -1):
    if i % 2 == 0 and i % 3 == 0:
        valid_number = i
        if valid_number == s:
            break
        else:
            print(valid_number, end=' ')

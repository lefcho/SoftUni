n = int(input())
count = 0

for x in range(n + 1):
    for y in range(n + 1):
        for z in range(n + 1):
            answer = x + y + z
            if n == answer:
                count += 1

print(count)
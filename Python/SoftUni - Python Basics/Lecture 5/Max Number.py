big = int(input())

while True:
    user = input()
    if user == 'Stop':
        break
    user = int(user)
    if user > big:
        big = user

print(big)

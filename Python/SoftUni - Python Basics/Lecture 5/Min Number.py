small = int(input())

while True:
    user = input()
    if user == 'Stop':
        break
    user = int(user)
    if small > user:
        small = user

print(small)

username = input()
password = input()
while True:
    data = input()
    if data == password:
        break
print(f'Welcome {username}!')
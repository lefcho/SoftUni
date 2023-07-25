def check_username(username: str):
    if len(username) < 3 or len(username) > 16:
        return False
    if "--" in username or "__" in username or "-_" in username or "_-" in username:
        return False
    for char in username:
        n = ord(char)
        if n == 45 or (48 <= n <= 57) or (65 <= n <= 90) or n == 95 or (97 <= n <= 122):
            continue
        else:
            return False
    return True


list_of_usernames = input().split(", ")

for username in list_of_usernames:
    if check_username(username):
        print(username)

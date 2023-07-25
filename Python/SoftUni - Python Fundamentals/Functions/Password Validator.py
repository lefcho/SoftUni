def length_check(password):
    length = 0
    for symbol in password:
        length += 1

    if 6 <= length <= 10:
        return True
    else:
        return False


def content_check(password):
    check = True
    for symbol in password:
        if 48 <= ord(symbol) <= 57 or 65 <= ord(symbol) <= 90 or 97 <= ord(symbol) <= 122:
            pass
        else:
            check = False
            break
    return check


def number_count(password):
    numbers = 0
    for char in password:
        if 48 <= ord(char) <= 57:
            numbers += 1
    if numbers < 2:
        return False
    else:
        return True


def password_check(password):
    if length_check(password) and content_check(password) and number_count(password):
        print("Password is valid")
    if not length_check(password):
        print("Password must be between 6 and 10 characters")
    if not content_check(password):
        print("Password must consist only of letters and digits")
    if not number_count(password):
        print("Password must have at least 2 digits")


user_password = input()

password_check(user_password)

message = input().split()
decrypted_msg = []
number = ""
second_part = ""

for word in message:
    m = ord(word[2])
    if 48 <= m <= 57:
        second_part = word[3::]
        number = (word[0] + word[1] + word[2])
        number = int(number)
    else:
        second_part = word[2::]
        number = int(number + word[0] + word[1])
    if len(second_part) > 1:
        temp = second_part[-1] + second_part[1:-1:] + second_part[0]
    else:
        temp = second_part
    decrypted_word = chr(number) + temp
    decrypted_msg.append(decrypted_word)

print(" ".join(decrypted_msg))
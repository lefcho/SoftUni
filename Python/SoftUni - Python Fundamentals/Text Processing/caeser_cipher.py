decrypted_version = input()
encrypted_version = ""

for char in decrypted_version:
    encrypted_version += chr(ord(char) + 3)

print(encrypted_version)
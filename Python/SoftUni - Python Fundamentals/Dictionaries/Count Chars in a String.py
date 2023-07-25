list_of_words = input().split()
dict_of_chars = {}

for word in list_of_words:
    for char in word:
        if char in dict_of_chars:
            dict_of_chars[char] += 1
        else:
            dict_of_chars[char] = 1

for char, count in dict_of_chars.items():
    print(f"{char} -> {count}")
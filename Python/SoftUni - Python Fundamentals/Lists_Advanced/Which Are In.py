key_words = input().split(", ")
words = input().split(", ")
final_list = []

for key in key_words:
    for word in words:
        if key in word and key not in final_list:
            final_list.append(key)

print(final_list)
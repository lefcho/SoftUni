def get_length(word1, word2):
    return len(word1), len(word2)

def check_len(word1, word2):
    if len(word1) == len(word2):
        return True
    return False


total_sum = 0

word_lst = input().split()
first_word = word_lst[0]
second_word = word_lst[1]
del word_lst

if check_len(first_word, second_word):
    for i in range(len(first_word)):
        total_sum += ord(first_word[i]) * ord(second_word[i])
else:
    len1, len2 = get_length(first_word, second_word)
    if len1 > len2:
        for i in range(len2):
            total_sum += ord(first_word[i]) * ord(second_word[i])
        remainder = len1 - len2
        second_part = first_word[-remainder:]
    elif len2 > len1:
        for i in range(len1):
            total_sum += ord(first_word[i]) * ord(second_word[i])
        remainder = len2 - len1
        second_part = second_word[-remainder:]

    for char in second_part:
        total_sum += ord(char)

print(total_sum)
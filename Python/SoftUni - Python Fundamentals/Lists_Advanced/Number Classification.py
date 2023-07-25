initial_list = [int(num) for num in input().split(", ")]
odd_list = [str(odd) for odd in initial_list if odd % 2 != 0]
even_list = [str(even) for even in initial_list if even % 2 == 0]
positive_list = [str(pos) for pos in initial_list if pos >= 0]
negative_list = [str(neg) for neg in initial_list if neg < 0]

print("Positive: " + ", ".join(positive_list))
print("Negative: " + ", ".join(negative_list))
print("Even: " + ", ".join(even_list))
print("Odd: " + ", ".join(odd_list))
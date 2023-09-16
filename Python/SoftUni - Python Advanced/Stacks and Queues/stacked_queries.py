num_of_queries = int(input())
stack = []
print_stack = []

for query in  range(num_of_queries):
    query_type = input()
    if query_type.startswith("1 "):
        query_type = [int(q) for q in query_type.split()]
        stack.append(query_type[1])
    elif query_type == "2" and stack:
        stack.pop()
    elif query_type == "3"and stack:
        print(max(stack))
    elif query_type == "4" and stack:
        print(min(stack))

while stack:
    print_stack.append(str(stack.pop()))

print(", ".join(print_stack))
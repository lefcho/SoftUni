parentheses_string = input()
stack = []
win = True

for parenthesis in parentheses_string:
    if parenthesis == '(' or parenthesis == '[' or parenthesis == '{':
        stack.append(parenthesis)
    elif stack:
        to_match = stack.pop()
        if to_match == '(' and parenthesis == ')':
            continue
        elif to_match == '[' and parenthesis == ']':
            continue
        elif to_match == '{' and parenthesis == '}':
            continue
        else:
            print("NO")
            win = False
            break
    else:
        print('NO')
        win = False
        break

if not stack and win:
    print('YES')
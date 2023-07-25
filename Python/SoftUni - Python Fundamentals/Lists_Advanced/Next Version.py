current_version = list(map(int, input().split(".")))
check = current_version[1]
next_version = current_version

if next_version[2] >= 9:
    next_version[2] = 0
    next_version[1] += 1
    if next_version[1] >= 9 and check >= 9:
        next_version[1] = 0
        next_version[0] += 1
    else:
        if next_version[2] != 0:
            next_version[1] += 1
else:
    next_version[2] += 1


next_version_string = (map(str, next_version))
print(".".join(next_version_string))

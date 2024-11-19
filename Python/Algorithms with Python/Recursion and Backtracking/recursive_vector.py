def generate01(idx, vector):
    if idx >= len(vector):
        print(*vector, sep='')
        return
    for num in range(2):
        vector[idx] = num
        generate01(idx + 1, vector)


n = int(input())

vec = [0] * n

generate01(0, vec)

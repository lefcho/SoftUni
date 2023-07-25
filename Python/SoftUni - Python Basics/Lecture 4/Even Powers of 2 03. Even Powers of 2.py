from math import pow

n = int(input())

for i in range(n + 1):
    if i % 2 == 0:
        answer = pow(2, i)
        print(f'{answer:.0f}')

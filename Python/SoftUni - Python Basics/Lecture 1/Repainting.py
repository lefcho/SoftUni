nylon = (int(input()) + 2) * 1.5
paint1 = int(input())
paint = (paint1 + paint1 * 0.1) * 14.5
thinner = int(input()) * 5
hours = int(input())
materials = nylon + paint + thinner + 0.4
workers = (materials * 0.3) * hours
print(materials + workers)

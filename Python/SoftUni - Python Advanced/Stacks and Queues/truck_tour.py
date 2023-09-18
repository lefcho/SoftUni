from collections import deque

petrol_pumps_amount = int(input())
petrol_pumps = deque([])
flag = False

for petrol_pump in range(petrol_pumps_amount):
    petrol_pumps.append([int(x) for x in input().split()])

for i in range(len(petrol_pumps)):
    win = True
    if flag:
        break
    gas = 0
    for pump in petrol_pumps:
        gas_charged = pump[0]
        km_to_next_pump = pump[1]
        gas += gas_charged
        gas -= km_to_next_pump
        if gas < 0:
            petrol_pumps.rotate(-1)
            win = False
            break

    if win:
        print(i)
        flag = True

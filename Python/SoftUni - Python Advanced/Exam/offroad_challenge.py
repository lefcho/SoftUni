from collections import deque

initial_fuel = [int(x) for x in input().split()]
consumption_indexes = deque(int(x) for x in input().split())
needed_quantities = deque(int(x) for x in input().split())

fail = False

for altitude in range(1, 5):
    fuel = initial_fuel.pop()
    consumption = consumption_indexes.popleft()
    needed_fuel = needed_quantities.popleft()
    fuel = fuel - consumption

    if fuel >= needed_fuel:
        print(f"John has reached: Altitude {altitude}")
        if altitude == 4:
            print("John has reached all the altitudes and managed to reach the top!")
    else:
        print(f"John did not reach: Altitude {altitude}")
        fail = True
        break
if fail:
    if len(needed_quantities) == 3:
        print("John failed to reach the top.")
        print("John didn't reach any altitude.")
    else:
        print("John failed to reach the top.")
        print("Reached altitudes: ", end='')
        for al in range(1, altitude):
            print(f"Altitude {al}", end='')
            if al != altitude - 1:
                print(", ", end='')

from collections import deque

quantity_of_food = int(input())
order_queue = deque([int(n) for n in input().split()])

print(max(order_queue))

while order_queue:
    if order_queue[0] <= quantity_of_food:
        quantity_of_food -= order_queue.popleft()
    else:
        print(f"Orders left: ", end="")
        for order in order_queue:
            print(order, end=" ")
        break

if not order_queue:
    print("Orders complete")
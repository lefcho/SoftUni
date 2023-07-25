from math import ceil

show_name = input()
runtime = int(input())
break_time = int(input())

lunch_time = break_time * 1/8
rest_time = break_time * 0.25

free_time = break_time - lunch_time - rest_time

if free_time >= runtime:
    left = free_time - runtime
    f_left = ceil(left)
    print(f'You have enough time to watch {f:"You have enough time to watch {show_name} and left with {f_left} minutes free time.')
elif free_time < runtime:
    needed = runtime - free_time
    f_needed = ceil(needed)
    print(f"You don't have enough time to watch {show_name}, you need {f_needed} more minutes.")

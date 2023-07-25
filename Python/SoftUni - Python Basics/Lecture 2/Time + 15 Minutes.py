current_hour = int(input())
current_minute = int(input())

f_minute = current_minute + 15
f_hour = current_hour

if f_minute >= 60:
    f_hour = current_hour + 1
    f_minute = f_minute % 60

if f_hour >= 24:
    f_hour = 0

if f_minute < 10:
    print(f"{f_hour}:0{f_minute}")
else:
    print(f"{f_hour}:{f_minute}")


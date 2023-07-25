from math import floor

record = float(input())
distance = float(input())
time_per_second = float(input())

swimming_time_before = distance * time_per_second
x = distance / 15
xx = floor(x)
slow_time = xx * 12.5
swimming_time = swimming_time_before + slow_time

if swimming_time > record:
    plus = swimming_time - record
    fplus = format(plus, '.2f')
    print(f"No, he failed! He was {fplus} seconds slower.")
elif swimming_time < record:
    f_swimming_time = format(swimming_time, '.2f')
    print(f"Yes, he succeeded! The new world record is {f_swimming_time} seconds.")

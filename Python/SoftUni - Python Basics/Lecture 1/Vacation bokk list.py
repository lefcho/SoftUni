from math import floor

pages = int(input())
p_per_hour = int(input())
days = int(input())
hours_per_day = (pages / p_per_hour) / days
print(floor(hours_per_day))
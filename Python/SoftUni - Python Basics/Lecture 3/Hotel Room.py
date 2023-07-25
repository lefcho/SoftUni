month = input()
nights = int(input())
studio = ''
apartment= ''

if month == 'May' or month == 'October':
    apartment = 65 * nights
    if nights > 14:
        studio = (50 * nights) * 0.7
    elif nights > 7:
        studio = (50 * nights) * 0.95
    else:
        studio = 50 * nights
elif month == 'June' or month == 'September':
    apartment = 68.7 * nights
    if nights > 14:
        studio = (75.2 * nights) * 0.8
    else:
        studio = 75.2 * nights
elif month == 'July' or month == 'August':
    apartment = 77 * nights
    studio = 76 * nights

if nights > 14:
    apartment = apartment * 0.9

print(f"Apartment: {apartment:.2f} lv.")
print(f"Studio: {studio:.2f} lv.")


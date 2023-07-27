cells = input().split("#")
water = int(input())
total_fire = 0
effort = 0
put_out_fires = []

for cell in cells:
    cell_list = cell.split(" = ")
    fire_level = cell_list[0]
    fire_power = int(cell_list[1])
    if fire_level == "High" and 81 <= fire_power <= 125:
        if water >= fire_power:
            water -= fire_power
            total_fire += fire_power
            effort += 0.25 * fire_power
            put_out_fires.append(fire_power)
    if fire_level == "Medium" and 51 <= fire_power <= 80:
        if water >= fire_power:
            water -= fire_power
            total_fire += fire_power
            effort += 0.25 * fire_power
            put_out_fires.append(fire_power)
    if fire_level == "Low" and 1 <= fire_power <= 50:
        if water >= fire_power:
            water -= fire_power
            total_fire += fire_power
            effort += 0.25 * fire_power
            put_out_fires.append(fire_power)


print("Cells:")
for fire in put_out_fires:
    print(f" - {fire}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")

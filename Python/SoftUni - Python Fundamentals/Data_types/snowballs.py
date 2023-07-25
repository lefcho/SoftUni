snowballs = int(input())
best_snowball = 0
best_weight = 0
best_time = 0
best_qlty = 0

for snowball in range(snowballs):
    weight = int(input())
    time = int(input())
    quality = int(input())
    current_ball = (weight / time) ** quality
    if current_ball > best_snowball:
        best_snowball = current_ball
        best_weight = weight
        best_time = time
        best_qlty = quality

print(f"{best_weight} : {best_time} = {round(best_snowball)} ({best_qlty})")


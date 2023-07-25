lenght = int(input())
widht = int(input())
height = int(input())
percent = float(input())
volume = (lenght * widht * height) * 0.001
print(volume * (1 - percent / 100))

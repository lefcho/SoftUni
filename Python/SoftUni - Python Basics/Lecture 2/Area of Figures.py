from math import pi

figure = input()

if figure == "square":
    sq_side = float(input())
    sq_area = pow(sq_side, 2)
    print(f"{sq_area:.3f}")
elif figure == "rectangle":
    rec_side1 = float(input())
    rec_side2 = float(input())
    rec_area = rec_side1 * rec_side2
    print(f"{rec_area:.3f}")
elif figure == "circle":
    cir_radius = float(input())
    cir_area = pi * cir_radius * cir_radius
    print(f"{cir_area:.3f}")
elif figure == "triangle":
    tri_side = float(input())
    tri_height = float(input())
    tri_area = (tri_height * tri_side) / 2
    print(f"{tri_area:.3f}")





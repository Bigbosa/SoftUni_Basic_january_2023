height_1 = float(input())
length = float(input())
height_2 = float(input())

window_width = 1.5

area = height_1 * length
window_area = window_width * window_width
all_countries = 2 * area - 2 * window_area
back_wall = height_1 * height_1
door = 1.2 * 2
full_back_and_front = 2 * back_wall - door
all_area = all_countries + full_back_and_front
green_paint = all_area / 3.4

roof = 2 * (height_1 * length)
roof_triangle_1 = 2 * (height_1 * height_2 / 2)
all_area_2 = roof + roof_triangle_1
red_paint = all_area_2 / 4.3

print(f"{green_paint:.2f}")
print(f"{red_paint:.2f}")
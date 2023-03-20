centimeters_long = int(input())
width = int(input())
height = int(input())
percent = float(input())

volume = centimeters_long * width * height

volume_in_liters = volume /1000

occupied_space = 0.17
need_liters = volume_in_liters * (1-0.17)

print(need_liters)
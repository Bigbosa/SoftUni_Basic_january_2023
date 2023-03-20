from math import floor
record_second = float(input())
meters = float(input())
time_in_seconds = float(input())

water_resistance = floor(meters /15)*12.5
total_time = time_in_seconds * meters + water_resistance

if total_time >= record_second:
    print(f"No, he failed! He was {total_time - record_second:.2f} seconds slower.")
else:
    print(f" Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
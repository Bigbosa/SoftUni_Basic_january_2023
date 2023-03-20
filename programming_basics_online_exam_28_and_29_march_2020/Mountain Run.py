record_in_second = float(input())
meters = float(input())
time_in_seconds_for_1m = float(input())

total_meters = meters * time_in_seconds_for_1m
total_meter_for_every_50m = int(meters /50) * 30

total_time = total_meters + total_meter_for_every_50m

if total_time < record_in_second:
    print(f" Yes! The new record is {total_time:.2f} seconds.")
else:
    diffrence = abs(total_time - record_in_second)
    print(f"No! He was {diffrence:.2f} seconds slower.")
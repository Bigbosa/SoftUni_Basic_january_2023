from math import ceil

serial_name = input()
episode_timeline = int(input())
time_for_break = int(input())

lunch = time_for_break /8
break_ = time_for_break /4

other_time = lunch + break_ + episode_timeline
time_left = time_for_break - other_time

if time_left >= 0:
    print(f"You have enough time to watch {serial_name} and left with {ceil(time_left)} minutes free time.")
else:
    print(f"You don't have enough time to watch {serial_name}, you need {ceil(abs(time_left)) } more minutes.")


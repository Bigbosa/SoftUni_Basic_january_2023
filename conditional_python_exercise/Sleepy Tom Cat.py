from math import floor
free_days = int(input())


minutes_ = 0
hours_ = 0
time_play = 30000

day_in_year = 365
time_for_break = 127
working_time = 63

break_days = free_days * time_for_break
work_day = (day_in_year - free_days) * working_time

sum_ = break_days + work_day
total_ = sum_ - time_play

hours_ = abs(total_) / 60
minutes_ = abs(total_) % 60

if sum_ >= time_play:
    print("Tom will run away")
    print(f"{floor(abs(hours_))} hours and {minutes_} minutes more for play")


else:
    print("Tom sleeps well")
    print(f"{floor(abs(hours_))} hours and {minutes_} minutes less for play")


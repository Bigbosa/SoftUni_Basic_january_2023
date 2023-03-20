from math import floor
first_racer = int(input())
second_racer = int(input())
third_racer = int(input())

total_time = first_racer + second_racer + third_racer

minutes = total_time // 60
seconds = total_time % 60

minutes = floor(minutes)

if seconds < 10:
    print(f"{minutes}:0{seconds}")
else:
    print(f"{minutes}:{seconds}")



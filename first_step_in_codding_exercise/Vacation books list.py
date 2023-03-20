number_of_page = int(input())
pages_for_one_hour = int(input())
number_of_days = int(input())

total_hour_a_day = number_of_page // pages_for_one_hour

needed_hours_on_day = total_hour_a_day/number_of_days

print(needed_hours_on_day)
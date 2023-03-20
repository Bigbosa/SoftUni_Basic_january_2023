month = input()
hours_spent = int(input())
num_people = int(input())
time_of_day = input()

hourly_rate = 0

if month in ["march", "april", "may"]:
    if time_of_day == "day":
        hourly_rate = 10.50
    else:
        hourly_rate = 8.40
else:
    if time_of_day == "day":
        hourly_rate = 12.60
    else:
        hourly_rate = 10.20


if num_people >= 4:
    hourly_rate *= 0.90


total = hourly_rate * hours_spent * num_people

if hours_spent >= 5:
    total *= 0.50
    hourly_rate *= 0.50




price_per_person = hourly_rate
print(f"Price per person for one hour: {price_per_person:.2f}")
print(f"Total cost of the visit: {total:.2f}")

day_in_week = input()

if day_in_week == "Monday" \
        or day_in_week == "Tuesday"\
        or day_in_week == "Wednesday" \
        or day_in_week == "Thursday"\
        or day_in_week == "Friday":
    print("Working day")
elif day_in_week == "Saturday" or day_in_week == "Sunday":
    print("Weekend")
else:
    print("Error")

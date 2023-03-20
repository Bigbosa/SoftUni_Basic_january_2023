number_of_people = int(input())
season = input()

percent = 0
total_sum = 0
total = 0

if number_of_people <= 5:
    if season == "spring":
       total =  number_of_people * 50

    elif season == "summer":
       total_sum =  number_of_people * 48.50
       percent = total_sum * 0.15
       total = total_sum - percent

    elif season == "autumn":
       total = number_of_people * 60

    elif season == "winter":
       total_sum =  number_of_people * 86
       percent = total_sum * 0.08
       total = total_sum + percent

if number_of_people > 5:
    if season == "spring":
        total = number_of_people * 48

    elif season == "summer":
     total_sum = number_of_people * 45
     percent = total_sum * 0.15
     total = total_sum - percent

    elif season == "autumn":
        total = number_of_people * 49.50

    elif season == "winter":
       total_sum = number_of_people * 85
       percent = total_sum * 0.08
       total = percent + total_sum

print(f"{total:.2f} leva.")


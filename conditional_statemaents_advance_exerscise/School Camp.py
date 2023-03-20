season = input()
group = input()
number_of_students = int(input())
number_of_night = int(input())

sport = 0
price = 0


if group == "boys":
   if season == "Winter":
       sport = "Judo"
       price = number_of_students * 9.60 * number_of_night
   elif season == "Spring":
       sport = "Tennis"
       price = number_of_students * 7.20 * number_of_night
   elif season == "Summer":
        sport = "Football"
        price = number_of_students * 15 * number_of_night

elif group == "girls":
    if season == "Winter":
        sport = "Gymnastics"
        price = number_of_students * 9.60 * number_of_night
    elif season == "Spring":
        sport = "Athletics"
        price = number_of_students * 7.20 * number_of_night
    elif season == "Summer":
        sport = "Volleyball"
        price = number_of_students * 15 * number_of_night

elif group == "mixed":
    if season == "Winter":
        sport = "Ski"
        price = number_of_students * 10 * number_of_night

    elif season == "Spring":
        sport = "Cycling"
        price = number_of_students * 9.50 * number_of_night


    elif season == "Summer":
        sport = "Swimming"
        price = number_of_students * 20 * number_of_night

if number_of_students >= 50:
    price = price * 0.50

elif 20 <= number_of_students < 50:
    price = price * 0.85

elif 10 <= number_of_students < 20:
    price = price * 0.95

print(f"{sport} {price:.2f} lv.")
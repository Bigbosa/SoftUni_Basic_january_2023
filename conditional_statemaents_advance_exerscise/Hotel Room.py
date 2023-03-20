month_ = input()
night = int(input())

studio = 0
apartment = 0


if month_ == "May" or month_ == "October":
    studio = 50
    apartment = 65
    if 7 < night <= 14:
        studio *= 0.95
    elif night > 14:
        studio *= 0.70


elif month_ == "June" or month_ == "September":
    studio = 75.20
    apartment = 68.70
    if night > 14:
        studio *= 0.80

elif month_ == "July" or month_ == "August":
    studio = 76
    apartment = 77

if night > 14:
    apartment *= 0.90

total_apartment = night * apartment
total_studios = night * studio


print(f"Apartment: {total_apartment:.2f} lv.")
print(f"Studio: {total_studios:.2f} lv.")

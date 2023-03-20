budget = float(input())
season = input()

class_car = 0
car = 0
price = 0
if budget <= 100:

    class_car = "Economy class"
    if season == "Summer" and budget:
        car = "Cabrio"
        price = budget *  0.35
    elif season == "Winter" and budget <= 500:
        car = "Jeep"
        price = budget  * 0.65
elif budget > 100:

    class_car = "Compact class"
    if season == "Summer" and budget <= 500:
        price = budget  * 0.45
        car = "Cabrio"
    elif season == "Winter" and budget <= 500:
        car = "Jeep"
        price = budget * 0.80

if budget > 500:
  class_car = "Luxury class"
  if season == "Summer" or season == "Winter":
     car = "Jeep"
     price = budget * 0.90

print(f"{class_car}")
print(f"{car} - {price:.2f}")


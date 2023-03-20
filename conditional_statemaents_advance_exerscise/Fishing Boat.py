all_budget = int(input())
season = input()
number_of_fishers = int(input())


full_price = 0

if season == "Spring":
    full_price = 3000
elif season == "Winter":
    full_price = 2600
else:
    full_price = 4200

if number_of_fishers <= 6:
    full_price *= 0.90

elif 7 <= number_of_fishers <= 11:
        full_price *= 0.85
else:
    full_price *= 0.75

if number_of_fishers % 2 == 0 and season != "Autumn":
        full_price *= 0.95

if all_budget >= full_price:
    print(f"Yes! You have {all_budget - full_price:.2f} leva left.")
else:
    print(f"Not enough money! You need {full_price - all_budget:.2f} leva.")
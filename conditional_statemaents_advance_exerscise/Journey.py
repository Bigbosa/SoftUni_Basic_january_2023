budget = float(input(""))
season = input()

place = 0
destination = 0
total_budget = 0

if budget <= 100:
    destination = "Bulgaria"

    if season == "summer":
        place = "Camp"
        total_budget = budget * 0.30
    else:
        place = "Hotel"
        total_budget = budget * 0.70
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        total_budget = budget * 0.40
        place = "Camp"
    else:
        place = "Hotel"
        total_budget = budget * 0.80

else:
   destination = "Europe"
   place = "Hotel"
   total_budget = budget * 0.90

print(f"Somewhere in {destination}")
print(f"{place} - {total_budget:.2f}")




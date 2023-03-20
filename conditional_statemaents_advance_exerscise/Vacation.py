budget = float(input())
season = input()

place = 0
location  = 0
price = 0

if budget <= 1_000:
    place = "Camp"
    if season == "Summer":
        location = "Alaska"
        price = budget * 0.65
    elif season == "Winter":
        location = "Morocco"
        price = budget * 0.45
elif budget > 1_000 or budget >= 3_000:
    place = "Hut"
    if season == "Summer":
        location = "Alaska"
        price = budget * 0.80
    elif season == "Winter":
        location = "Morocco"
        price = budget * 0.60
if budget > 3_000:
    place = "Hotel"
    if season == "Summer":
        location = "Alaska"
        price = budget * 0.90
    elif season == "Winter":
        location = "Morocco"
        price = budget * 0.90
print(f"{location} - { place} - {price:.2f}")



season = input()
km_for_month = float(input())

price = 0
total = 0


if km_for_month <= 5_000:

    if season == "Spring" or season == "Autumn":
        price = km_for_month * 0.75
        total = (price * 4) * 0.90


    elif season == "Summer":
        price = km_for_month * 0.90
        total = (price * 4) * 0.90


    elif season == "Winter":
        price = km_for_month * 1.05
        total = (price * 4) * 0.90


elif 5_000 < km_for_month <= 1_0000:

    if season == "Spring" or season == "Autumn":
        price = km_for_month * 0.95
        total = (price * 4) * 0.90


    elif season == "Summer":
        price = km_for_month * 1.10
        total = (price * 4) * 0.90


    elif season == "Winter":
        price = km_for_month * 1.25
        total = (price * 4) * 0.90


if 1_0000 < km_for_month <= 2_0000:

    if season == "Spring" or season == "Autumn" or season == "Summer" or season == "Winter":
        price = km_for_month * 1.45
        total = (price * 4) * 0.90


print(f"{total:.2f}")
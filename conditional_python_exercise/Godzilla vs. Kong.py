buget = float(input())
extras = int((input()))
clothing_price = float(input())

decor = buget * 0.10

if extras > 150:
    clothing_price *= 0.90


full_price = decor + extras * clothing_price


if full_price <= buget:
    print("Action!")
    print(f"Wingard starts filming with {buget - full_price:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {full_price - buget:.2f} leva more.")





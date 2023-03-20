import math
name_of_football_fen = input()
budget = float(input())
beer_bottle = int(input())
number_chips = int(input())

for_one_bottle_beer = 1.20



price = beer_bottle * for_one_bottle_beer
price_2 = price * 0.45

total_price_for_chips = price_2 * number_chips
all_price = price + math.ceil(total_price_for_chips)

if all_price <= budget:
    print(f"{name_of_football_fen} bought a snack and has {budget - all_price:.2f} leva left.")
else:
    print(f"{name_of_football_fen} needs {all_price - budget:.2f} more leva!")

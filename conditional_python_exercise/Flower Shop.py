import math
number_of_magnolias = int(input())
number_of_hyacinths = int(input())
number_of_rose = int(input())
number_of_cactus = int(input())
present_price = float(input())

MAGNOLIAS = 3.25
HYACINTHS = 4
ROSE = 3.50
CACTUS = 8
taxes = 0.5

total_price = number_of_magnolias * MAGNOLIAS \
              + number_of_hyacinths * HYACINTHS \
              + number_of_rose * ROSE \
              + number_of_cactus * CACTUS

total_taxes = total_price - ((total_price * taxes) / 10)


if present_price > total_taxes:
    total_taxes = present_price - total_taxes
    print(f"She will have to borrow {math.ceil(total_taxes)} leva.")
else:
    total_taxes = total_taxes - present_price
    print(f"She is left with {math.floor(total_taxes)} leva.")
nylon = int(input())
paint = int(input())
thinner = int(input())
working_hours = int(input())


NYLON = 1.50
PAINT = 14.50
THINNER = 5.00
BAGS_PRICE = 0.40

nylon += 2
paint += paint * 0.10

material_price = (nylon * NYLON)\
                 + (paint * PAINT)\
                 + (thinner * THINNER)\
                 + BAGS_PRICE

price_for_hour = material_price * 0.30

final_price = material_price + (price_for_hour * working_hours)

print(final_price)
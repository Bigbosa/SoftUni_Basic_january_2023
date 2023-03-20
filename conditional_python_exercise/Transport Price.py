n_km = int(input())
parth_of_day = input()

STARTER_PRICE = 0.70
DAY_PRICE = 0.79
NIGHT_PRICE = 0.90
bus = 0.09
train = 0.06

total_price = 0

if n_km < 20:
    if parth_of_day == "day":
     total_price = STARTER_PRICE + n_km * DAY_PRICE

    else:
      total_price = STARTER_PRICE + n_km * NIGHT_PRICE

elif n_km < 100:
    total_price = n_km * bus

elif n_km >= 100:
    total_price = n_km * train


print(f"{total_price:.2f}")
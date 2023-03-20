fish_1_price = float(input())
fish_2_price = float(input())
fish_3_kilogram = float(input())
fish_4_kilogram = float(input())
mussels = int(input())

fish = fish_1_price + fish_1_price * 0.60

price_fish_ = fish_3_kilogram * fish

fish_2 = fish_2_price + fish_2_price * 0.80

price_fish_2 = fish_4_kilogram * fish_2

mussels_sum = mussels * 7.50

total_sum = price_fish_ + price_fish_2 + mussels_sum

print(f"{total_sum:.2f}")

price_for_bags = float(input())
kg_bags = int(input())
day_travel = int(input())
number_bags = int(input())

price = 0
price_2 = 0

if kg_bags < 10:
    price = price_for_bags * 0.20

elif kg_bags >= 10 and kg_bags <= 20:
    price = price_for_bags * 0.50

else:
    price = price_for_bags

if day_travel > 30:
      price_2 = price * 0.10

elif day_travel >= 7 and day_travel <= 30:

    price_2 = price * 0.15
elif day_travel < 7:
    price_2 = price * 0.40

total_sum = (price + price_2) * number_bags

print(f"The total price of bags is: {total_sum:.2f} lv. ")
import math
number_of_days = int(input())
food_kg = int(input())

dog_food_kg = float(input())
cat_food_kg = float(input())
turtle_food_g = float(input())

total_sum = 0

dog_food_sum = number_of_days * dog_food_kg
cat_food_sum = number_of_days * cat_food_kg
turtle_food_sum = (number_of_days * turtle_food_g) / 1000

total_sum = dog_food_sum + cat_food_sum + turtle_food_sum

if total_sum <= food_kg:
    print(f"{math.floor(food_kg - total_sum)} kilos of food left.")
else:
    print(f"{math.ceil(total_sum - food_kg)} more kilos of food are needed.")
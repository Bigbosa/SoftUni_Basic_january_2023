number_of_days = int(input())
capacity_food = float(input())

biscuits = 0
eaten_dog_food = 0
eaten_cat_food = 0

for day in range(1, number_of_days + 1):
    total_eat_food_dog = int(input())
    total_eat_food_cat = int(input())
    eaten_dog_food += total_eat_food_dog
    eaten_cat_food += total_eat_food_cat

    if day % 3 == 0:
        biscuits += (total_eat_food_dog + total_eat_food_cat) * 0.10

total_food_for_all_days = eaten_dog_food + eaten_cat_food
percent_food = (total_food_for_all_days / capacity_food) * 100
percent_dog_food = (eaten_dog_food / total_food_for_all_days) * 100
percent_cat_food = (eaten_cat_food / total_food_for_all_days) * 100

print(f"Total eaten biscuits: {round(biscuits)}gr.")
print(f"{percent_food:.2f}% of the food has been eaten.")
print(f"{percent_dog_food:.2f}% eaten from the dog.")
print(f"{percent_cat_food:.2f}% eaten from the cat.")


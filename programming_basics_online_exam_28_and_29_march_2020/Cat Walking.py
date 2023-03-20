minutes_walking = int(input())
walks = int(input())
calories = int(input())

total_minutes_walking = minutes_walking * walks

total_lose_calories = total_minutes_walking * 5

cat_need_to_lose_calories = calories * 0.5

if total_lose_calories >= cat_need_to_lose_calories:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {total_lose_calories}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {total_lose_calories}.")




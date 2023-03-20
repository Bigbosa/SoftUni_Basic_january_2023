import  math
number_of_day = int(input())
left_food = int(input())
food_for_first_deer = float(input())
food_for_second_deer = float(input())
food_for_the_third_deer = float(input())

need_food = number_of_day * food_for_first_deer
need_food_2 = number_of_day * food_for_second_deer
need_food_3 = number_of_day * food_for_the_third_deer

total_food = need_food + need_food_2 + need_food_3
if total_food <= left_food:
    print(f'{math.floor(left_food - total_food)} kilos of food left.')
else:
    print(f'{math.ceil(total_food - left_food)} more kilos of food are needed.')
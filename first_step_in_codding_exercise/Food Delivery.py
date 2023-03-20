numbers_of_soup = int(input())
number_fish_food = int(input())
Vegetarian_food = int(input())


CHICKEN_MENU_PRICE = 10.35
MENU_FISH_PRICE = 12.40
VEGETARIAN_MENU_PRICE = 8.15

delivery = (numbers_of_soup * CHICKEN_MENU_PRICE) \
                  + (number_fish_food * MENU_FISH_PRICE) \
                  + (Vegetarian_food * VEGETARIAN_MENU_PRICE)

desert = delivery * 0.20
delivery_price = delivery + desert + 2.50

print(delivery_price)



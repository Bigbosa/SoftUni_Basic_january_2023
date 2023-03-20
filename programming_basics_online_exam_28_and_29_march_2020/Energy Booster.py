text = input()
text_2 = input()
steck_with_gels = int(input())

sum_ = 0
number_in_set = 0

WATERMELON_for_2 = 56
WATERMELON_for_5 = 28.70

MANGO_for_2 = 36.66
MANGO_for_5 = 19.60

PINEAPPLE_for_2 = 42.10
PINEAPPLE_for_5 = 24.80

RASPBERRY_for_2 = 20
RASPBERRY_for_5 = 15.20

if text_2 == "big":
    number_in_set = 5
    if text == "Watermelon":
       sum_ = WATERMELON_for_5
    elif text == "Mango":
        sum_ = MANGO_for_5
    elif text == "Pineapple":
        sum_ = PINEAPPLE_for_5
    elif text == "Raspberry":
        sum_ = RASPBERRY_for_5

if text_2 == "small":
    number_in_set = 2
    if text == "Watermelon":
       sum_ = WATERMELON_for_2
    elif text == "Mango":
        sum_ = MANGO_for_2
    elif text == "Pineapple":
        sum_ = PINEAPPLE_for_2
    elif text == "Raspberry":
        sum_ = RASPBERRY_for_2

total_price = number_in_set * sum_ * steck_with_gels

if 400<= total_price <= 1000:
    total_price*=  0.85
elif total_price > 1000:
    total_price *= 0.50

print(f"{total_price:.2f} lv.")




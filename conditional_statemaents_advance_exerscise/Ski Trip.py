day_for_staying = int(input()) - 1
room_ = input()
evaluation = input()

price = 0

if room_ == 'room for one person':
    price = 18
elif room_ == 'apartment':
    price = 25
    if day_for_staying > 15:
        price *= 0.50
    elif day_for_staying >= 10:
        price *= 0.65
    else:
        price *= 0.70
elif room_ == 'president apartment':
    price = 35
    if day_for_staying > 15:
        price *= 0.80
    elif day_for_staying >= 10:
        price *= 0.85
    else:
        price *= 0.90

if evaluation == "positive":
    price *= 1.25
elif evaluation == "negative":
    price *= 0.90

total_sum = price * day_for_staying

print(f"{total_sum:.2f}")
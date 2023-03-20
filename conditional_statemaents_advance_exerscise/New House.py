flowers = input()
number_of_flowers = int(input())
budgets = int(input())

total_price = 0

rose = 5.00
Dahlias = 3.80
Tulips = 2.80
Narcissus = 3
Gladiolus = 2.50

if flowers == "Roses":
    total_price = number_of_flowers * rose

    if number_of_flowers > 80:
        total_price *= 0.90

elif flowers == "Dahlias":
    total_price = number_of_flowers * Dahlias

    if number_of_flowers > 90:
        total_price *= 0.85

elif flowers == "Tulips":
    total_price = number_of_flowers * Tulips

    if number_of_flowers > 80:
        total_price *= 0.85

elif flowers == "Narcissus":
    total_price = number_of_flowers * Narcissus

    if number_of_flowers < 120:
        total_price *= 1.15

elif flowers == "Gladiolus":
    total_price = number_of_flowers * Gladiolus

    if number_of_flowers < 80:
        total_price *= 1.20

if total_price <= budgets:
    print(f"Hey, you have a great garden with {number_of_flowers} {flowers} and {budgets - total_price:.2f} leva left.")
else:
    print(f"Not enough money, you need {total_price - budgets:.2f} leva more.")

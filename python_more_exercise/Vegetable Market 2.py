vegetables = float(input())
fruits = float(input())
all_kilograms_vegetables = int(input())
all_kilograms_fruits = int(input())

sum_1 = vegetables * all_kilograms_vegetables
sum_2 = fruits * all_kilograms_fruits

all_sum = sum_1 + sum_2
euro = all_sum / 1.94

print(f"{euro:.2f}")


